# Making a Blog using Flask
It's been awhile since I've tried making a blog again, but instead of using Jekyll and md files (which might get me up and running in under an hour), I'm going to use Flask. Should be fun.

I think one of the things I also want to work on learning better is Docker, as well as Makefile.

## Tech
- Flask (server code and presentation)
- postgres (backend db)
- gunicorn (WSGI HTTP server)
- Docker (container)
- Makefile (build scripting)
- WSL2 (local development)
- TBD - either Heroku, Netlify, LightSail, or other (hosting)
- TBD (data layer hosting)

## Repository
https://github.com/mmcintyre1/silently-failing


## Starting out - Getting the Dev Environment Up and Running
I think my first step is going to be getting a simple Flask app functioning in a docker container, then deploying that to Netlify. If I can start with the CI/CD so I can easily push changes live, it'll allow me to concentrate on the stuff I know less well -- presentation. The last app I hosted on Netlify was a jekyll app, so there was no data layer. Doesn't seem like netlify offers any database services, but I can probably find something easy enough.

## Making the Repository and a Simple Flask App
All right, step 1 is making a repository structure for the Flask app. Flask recommends [this structure](https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/), so that's what I've gone with. I've got the project structure in [this commit](https://github.com/mmcintyre1/silently-failing/tree/b702777d1307d8c8362d45dd39e5754c7ff69b6d). I made `templates` and `static` folder as well, but they are empty so won't be committed yet.

I've created a virtual environment by using the command `python -m venv venv` and then running `pip install flask`.

I can run this locally easily enough. First I run `export FLASK_APP=silently-failing`, then I run `flask run`. This will get me up and running locally. Looks like shit, but you have to start somewhere.

## Getting Docker and Docker Desktop with WSL2
Since I'm running in WSL2, I'm using Docker Desktop to make my life easier. I could probably run docker directly in WSL2, but Docker and Windows make that really silly. There's a pretty good rundown of [Docker's integration with WSL2](https://www.docker.com/blog/new-docker-desktop-wsl2-backend/).

I used the Windows docs for [getting started with Docker and WSL2](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers). As a side note, Microsoft's documentation is normally exceptional. They have really upped their game.

## Doing the Docker thing
So now I need to build the docker container image, then run that container image. We can write out the instructions for building that container image in a `Dockerfile`, then we can build the container image via `docker build` then we can run that container via `docker run`. I'm following [Docker's guide](https://docs.docker.com/language/python/build-images/). [This](https://github.com/mmcintyre1/silently-failing/blob/afe7e4d3bfc4d1e3c550a4a8319b292dd441dd9f/Dockerfile) is what my `Dockerfile` looks like right now.

Now I can build the image using the command `docker build --tag silently-failing .` while in my applications root directory. Giving the image a name will make it easier to run commands later. The tag is in the format of `name:tag`, and leaving off the tag omits it from the image.

Then, I can run the image container via `docker run -d -p 5000:5000 silently-failing`.
- `-d` means in detached mode, so it runs in the background
- `-p` publishes the ports within the container to outside the container
- `silently-failing` tells it what image to run.

### Docker and caching, and some best practices
One interesting thing about docker is that each command is a layer, and there is a cache that is maintained that means every time you run `docker build` docker will look for an existing layer in its cache, and if one exists it uses that instead of building a new one. This build cache is super important, and it's why you see things like these commands separated:

```docker
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app
```

This is a really helpful page to read through:
[Best practices for writing a Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

There is also a bit of chatter on running Docker images as root user and how you generally shouldn't be doing it. Since a docker container is running on the same kernel as the host, there isn't the typical separation of layers that you might see with a virtual machine. For some use cases it doesn't really matter since the application you might run doesn't actually run as root, for example, nginx.

### Difference Between `CMD` and `ENTRYPOINT`
I've written my `Dockerfile` with `CMD`, but I've seen `ENTRYPOINT` used as well. [Here's](https://www.bmc.com/blogs/docker-cmd-vs-entrypoint/#) a pretty decent resource on the topic, but it seems to boil down to whether or not you want your commands to be able to overridden at the command line when starting the image. Your `Dockerfile` needs either a `CMD` or an `ENTRYPOINT`. I'm using the command `python3 -m flask run --host=0.0.0.0`, but if I wanted to use `python3 -m flask shell`, I can do that easily by running the command `docker run silently-failing flask shell`.

## Adding in Gunicorn
So now I want to add in a web server to replace the simple one Flask gives. The web server just needs to implement WSGI and will integrate with Flask as Flask is expecting WSGI. The [wikipedia for WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) is a pretty good resource for more information. Need to update the Dockerfile. I'm loosely using [this](https://itnext.io/setup-flask-project-using-docker-and-gunicorn-4dcaaa829620) as a resource, but instead of using a shell script I'll just pass in the start up commands via `CMD`. [This](https://github.com/mmcintyre1/silently-failing/blob/365d3c739f4c0fae2d3686728718bc709481a760/Dockerfile) is what my `Dockerfile` looks like now.

Another thing I've noticed is that in working with docker, I am running `docker build` a bunch, and I have a ton of images I need to go through and delete. This is easy enough via Docker Desktop, but surely there is a better way to manage the lifecycle of these containers and clean up detritus.

## Simplifying Docker Stuff with Docker Compose
Typically Docker Compose is used to run multi-container apps, like if we were going to run a flask/gunicorn container, an nginx container, and postgres container all with the same `docker-compose` command. It also makes it much lighter than typing out the same long-winded `docker run -d -p 8050:8050 silently-failing`, and it allows me to mount volumes outside of the container to within the container so I don't need to constantly be rebuilding the container itself after every file update.

[Putting together a docker-compose.yml file](https://github.com/mmcintyre1/silently-failing/blob/ef1c5523c38f0f00d1c18c746801314eb5aca15d/docker-compose.yml) was easy as pie using [this](https://docs.docker.com/compose/gettingstarted/) documentation, but I spent a bit longer than I'm comfortable admitting working on how to get hot reloading working. At first I was futzing around with the mounted drives, then I was trying to pass in environment variables via a `.env` file and the `env_file` command in the `docker-compose.yml` file (I might go back to this, as the way I currently have it is using `debug=True` in the `main` block in my flask app file). Finally, I realized that I was missing a `--reload` directive to my gunicorn command. Adding that in, and things worked perfectly. Just needed to go back and clean up all the things that didn't work, since I was kind of throwing things at the wall for a bit there and I'm not sure what the side effects are of things I was doing.

Anyway, on to a simple makefile.

## Making make files
So a makefile should give us a nice entry into build and run commands. I don't think I need to run gunicorn in dev since the Flask HTTP server is suitable. There might be some argument to running gunicorn in dev just so dev and live are as synonymous as possible ([12 Factor App: Dev/prod parity](https://12factor.net/dev-prod-parity)). I don't really have an opinion right now.

The commands I think I want are
- build
- run-dev
- run-live
- kill

The way I implemented this for now is to have separate commands for dev and live, but I think I'd much rather be able to set an environment variable for development or production and have that determine what needs to run. Less overhead and duplication maybe? [Relevant commit](https://github.com/mmcintyre1/silently-failing/tree/622f95f089d095c16b07e006dd9a12d3d2ceeaa6)

## Building and Hosting the application
### Netlify or something else?
So when choosing a platform to run my blog, I had originally thought Netlify, but Netlify only hosts static content. Makes sense for a jekyll blog since it's a glorified router to md files, but for flask which needs to run a backend server so Netlify isn't as suitable. I heard something about Netlify functions, but that means the architecture of the app would need to change. I'm not sure if the idea is you'd have server functions like getting a blog post or deleting a blog post implemented each in a function and your web server is just routing to those functions and controlling presentation? Anyway, seems a bit too complicated. I just want to point a hosting site at a github repo, tell it to redeploy on updates to master, give it a command to run to start my web server, and potentially give me access to a data layer.

### Heroku
Some options for Flask that I've heard are pythonanywhere and Heroku. Heroku is the first one I tried and seems to fit all the use cases, but it's what I'm going with for now. If I want to change it in the future it shouldn't be too hard. I have my DNS taken care of by Route 53 in AWS, so changing backend is just swapping where my CNAME points.

Another option was some of the options one step up from free, so things like EC2, Lightsail, Azure, etc. The downside is those cost money, I'd have to spin my own CI and CD (using GitHub actions makes that relatively trivial), and the other options are free. Free tier is the only thing that makes sense for small sites. The idea is that your low traffic site is being subsidized by the big players, so paying early on in a site's existence doesn't make a ton of sense, especially when elastically growing into a paid tier is so easy.

First thing is create a Heroku account. I did that through the web UI. Don't forget MFA!

After that, I worked primarily with the CLI in my WSL. I ran into a problem where I created the site in the web UI first, then I couldn't figure out the command to switch apps in the CLI, so I ended up deleting the site and just running `heroku create silentlyfailing` through the CLI.

I was interested in how heroku was using git and [here](https://stackoverflow.com/questions/5338551/how-does-git-push-heroku-master-know-where-to-push-to-and-how-to-push-to-a-dif) is a good Stack Overflow answer on it. It works like how you would expect git to work, but I haven't used git for anything other than GitHub, so it's cool to see the tech.

The tutorial I was generally following was [Heroku's own](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

#### Heroku Dynos
I'm not sure where the term "dynos" comes from, but these represent container types available. In practice, they are a way to gate certain functionality. For me, I was concerned with two things: 1) uptime 2) HTTPS. With the free dyno, you have to manage your own HTTPS certificates, and your site is taken offline after 30 minutes of inactivity before being started again. For the $7 a month hobby dyno, you get managed certs and no downtime, which seems like a small investment. Additionally, the price is prorated to uptime, so if you take your site down you aren't paying for capacity. More information on dynos [here](https://dev.to/milandhar/what-are-heroku-dynos-3b1p).

#### Heroku Procfiles
Once Heroku starts up a server, I need to give it a command so it knows what it should do. This takes the form of a `Procfile`. For now mine is very simple: `web: gunicorn silentlyfailing:app`. This `Procfile` represents a divergence from how the app runs locally, which is through docker. You can run the `Procfile` locally through `heroku local web`, but I found you need to install requirements and the database won't work, so I will prefer to use docker for now. The risk is that I need to manually keep my dev environment and the Heroku environment similar, but that isn't such a large problem for such a small app.

### DNS Stuff
Heroku, like all hosting sites, uses some sort of variation on {your-app-name}.{sites-base-name}.com. I used [Heroku's guide on configuring your site with Route 53](https://devcenter.heroku.com/articles/route-53). I have my apex domain, `silentlyfailing.com` redirecting to an S3 bucket, which is then redirecting to `www.silentlyfailing.com`, which is ultimately pointed to Heroku's DNS servers. You also need to add your domains to Heroku, either via the CLI or within the UI. Not sure why, but Heroku says it's to "to properly route traffic for specific domains to the right application on Heroku". I'm not smart enough to parse that one out. Maybe some header information?

On the alias record to direct to an S3 bucket back to the www subdomain, Heroku doesn't provide an explanation other than to say "Your domain example.com now redirects to www.example.com in a scalable way". Is there something scalable, or is this a way to easily add subdomains? Not sure on this one either, I'm barely above drowning when it comes to network stuff. One day I need to sit down and read all about this stuff.

### Deploying
Since Heroku manages files via git, you could push your code directly to your app via git commands and setting the remote to your heroku app, but since I'm already using GitHub, I think it's easier to just enable the GitHub integration that already exists. You integrate your GitHub and Heroku accounts, point Heroku to the relevant repository, and off it goes. I think it works by setting up webhooks that trigger commits to master in your GitHub repository to push those changes out to your heroku app and trigger a rebuild your heroku app. But things just work. Now on to actually working on the app.

## Time to Actually Make the Damn Blog
But before that, I had to do some quick work with my make commands to change how they pulled environment variables. I was declaring my `FLASK_APP` all over the place, so instead, I could just include a reference to my .env.dev in my `Makefile` and the `docker-compose-dev.yml` file, and then I could call the environment variable via `${FLASK_APP}`. This way, I only need to change it in one spot, that .env file.

### Secret Keys and Factories
I was reading through [Flask's Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/) and they have you create an application factory, so I borrowed the logic there to create things. They recommend a `SECRET_KEY` so I have one I've plopped into my `.env.sample` file as well as one I have on Heroku, so I can do something simple like this: `SECRET_KEY=os.getenv('SECRET_KEY', 'dev')` to and pass that into `app.config.from_mapping()` to set a secret key for dev and live. The only other thing I had to update when I changed from an app to an app factory was the reference in my `manage.py`. Originally, I was importing app from silentlyfailing, but now I import my `create_app` function and pass that into the `FlaskGroup` init. [Code here](https://github.com/mmcintyre1/silently-failing/tree/411a7222be500d46a0ef269875cc3b0d6a5a2d65).

Quick update -- this failed to deploy, so I needed to update my `Procfile` to `web: gunicorn "silentlyfailing:create_app()"` to actually call the function, which took care of the deploy.

### Doing the Database Thing
So now I need to make a database to store all my wonderful blog posts and musings. I think the idea here is to use sqlalchemy to encapsulate database creation, and alembic to handle migrations. The first step here is getting a postgres instance up and running locally, so I'll first need to modify my docker-compose file to add in the postgres service, then I'll need to probably update my app factory to connect to the database and pull whatever connection variables it needs from the environment, then build out some database models, etc., etc. Finally, I'll need to update my Heroku app to start the server and run the database migrations via alembic. After I get all this done, I should finally be able to start building out the application.

#### A note about backups
One of my considerations here is actually whether the data in my heroku postgres is reliably stored, and whether it persists in some fashion or another. The blog posts themselves will reside within the database, and they are the value prop here, so I'd hate to lose them. One avenue I could explore would be to use Flask to render static content via markdown files and not require a database at all. I'm not sure flask is suited for static sites or if there is an alternative technology that might be better. Need to do some investigation. I think I'd feel more comfortable hosting on RDS, but from experience that runs $15-30 a month for micro or small t instances.

#### Setting up my dev postgres
So the first thing I did was set up the postgres service in my local dev environment. I needed to add in some environment variables, and according to the [postgres Docker documentation](https://hub.docker.com/_/postgres) the only required environment variable is `POSTGRES_PASSWORD`, but I included each element of the URI string in environment variables. I updated the [docker compose file](https://github.com/mmcintyre1/silently-failing/commit/96e8be654ccb57b588c102cdd413d10ce2feaf7e), and then I modified the way configuration variables were passed in to the application by using a `config.py` [file with some minor inheritance](https://github.com/mmcintyre1/silently-failing/commit/e15acf8490a7e750cceb797aac726485f895c0ad). One of the workarounds I had to do was in the `ProductionConfig` class, the environment variable is different on Heroku -- they give you a full `DATABASE_URL` as opposed to each element, so there is some inconsistency with dev and live. In the future I'd like to modify this to be more consistent. Since all three of those config classes are evaluated at runtime, I had to replace `os.environ[KEY]` with `os.getenv(KEY, default_value)` since those environment variables aren't set in live. I might be able to break up that `DATABASE_URL` heroku gives into individual parts.

I also [updated the `Makefile`](https://github.com/mmcintyre1/silently-failing/commit/95973ea8c3f9a91209161573f187987cdeba6747) to include killing off the db container in addition to the web container.

Finally, I needed to do a quick modification of the `DATABASE_URL` that Heroku gives me, since SQLAlchemy is expecting postgresql, not postgres, at the beginning of the URI.

#### Setting up SQLAlchemy
I want to use an ORM here so I don't need to worry about database-specific semantics. The general recommendation here is SQLAlchemy, but I've also heard peewee recommended. I've worked with SQLAlchemy in the past, so that's what I've used here. I created a `models.py` [file](https://github.com/mmcintyre1/silently-failing/commit/df8bc6cf987296bb30fe5002ddd67bdd4401b42d), initialized a SQLAlchemy database instance, and defined a really simple `Cats` model for testing purposes. I simplified the app factory, removing superfluous things for now (I'll probably add back in the `test_config` if/else so I can pass in test_config parameters for testing purposes by creating an instance of the app). One other item I needed to take care of was because I am using the [application factory pattern](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/) (the primary use case seems to be for either testing or process-sharing purposes), I needed to push an application context so the database could use it. Looks something like this:

```python
with app.app_context():
    db.init_app(app)
    db.create_all()
```

I'm not entirely sure what an app context is, but there is more [information here](https://flask.palletsprojects.com/en/2.0.x/appcontext/). I think more might be revealed as I continue work on the blog and add in tests.

One other item of note is that running against postgres in SQLAlchemy requires some additional binaries, so I needed to updated the `Dockerfile` to [install those binaries](https://github.com/mmcintyre1/silently-failing/commit/51e2c807d7bd1f9eadcf5a0337f8c71c6fd587af), and pip installed psycopg2 and psycopg2-binaries.

From here, I can connect to both my local postgres and heroku postgres, and I see that the table is created.

#### Setting up Alembic for migrations
Last bit before I can actually work on the app, but I want to use a utility to track database migrations. I don't anticipate a ton of changes to the database schema, but migrations are a great way to track schema changes and iteratively develop without destroying all your previous data. Alembic is a great library for doing this.

The idea with Alembic is to create a Migration object, associate your app with it, then run the commands `flask db init` to create a migrations folder and seed it with some files. Then you can run `flask db migrate` to generate a revision file that you manually review. Everything within the migrations folder gets checked in to github. Alembic will essentially compare your models to the database and generate a diff and the SQL statements will be generated and called via python code. Finally, when you deploy, you can add a little command to Heroku (semi-colon delimited) to run all the migrations to get the live database up to date with your newly pushed schema.

I'm starting to get my mind around how these extensions work. [This stackoverflow answer](https://stackoverflow.com/questions/19750060/how-to-properly-initialise-the-flask-sqlalchemy-module) is super helpful in breaking down what that `init_app` does and when to use it and when not to use it.

I also updated the docker-compose file to handle migrations in a separate container. These migrations run once, then the container is removed. Breaking it out this way makes it easy to modify that particular part of the compose, or remove it as needed. Tidy separation of purposes. Right now the migrations could still just be called as part of the web container by adding the upgrade db call to the command, but this gives me a bit of flexibility in the future.

I ran into a weird problem that I need to investigate though, which is that my configuration file does not seem to be pulling from environment variables I set in the docker-compose. I have my environment set on the docker-compose for my `POSTGRES_HOST` to be `postgres`, but in the `DevelopmentConfig` class in the `config.py` file, I am using `os.getenv('POSTGRES_HOST', 'localhost')`. When the flask app running in a docker container needs to connect to the postgres database, the internal network docker sets up will have the host be the container name, in this case postgres. But outside of the container, I can connect to it via localhost. All of this is to say that the flask app in the container is pulling the default value, so I must be missing environment variables somewhere.

*Workaround to the above* -- I figured out what was happening. I was setting the `POSTGRES_HOST` on the db container, not the web container in my docker-compose. Passing in the `POSTGRES_HOST` via the .env.dev file, which is only used by docker and the Makefile, means I can set the default to localhost, so I can run the flask server via the command line outside of the container while the database is up inside the container.

Once I run docker-compose, I have 4 services, the `base` image, the `web` image, the `migrations` image and the `postgres` image. I can connect to the database just using localhost since I've published the ports.

One final item: I added a bit to the docker-compose to ensure that the web and migrations service don't start until the database is up. The way I achieved this was to add a healthcheck to the db service, then add in a `depends` on the db with a condition for the service to be healthy to the web and migrations service. I can't add to the base service because services with `depends on` can't be extended.

**MM's note: I seem to use containers and services interchangeably. Need to hammer out that vocabulary.

### Building the models and controllers
I am going to separate presentation entirely from how I get or post data. That way, I can swap out front end easily. You could probably pass python objects directly to the view to render, by I think I'll prefer to pass json objects to the views.

What I think I need to do here is to create a blog model, a method to get blog objects from the database, and a method to write blog objects to the database. I probably also need a login method, or some way to prove I'm admin and keep me in an authenticated session. I want to wrap that method to write in some sort of authentication. I probably don't need to store any user info in the database, just check a password against some environment variable.

#### Setting up an admin account and login/logout
I want to be able to have a single admin account that is allowed to create, update, and delete blog posts. This means I need to also have a login mechanism, as well as write that username and password to the database.

I am using the flask-login library, which handles session data for logging a user in or out. From what I can see, it provides convenience functions and decorators for setting app state about a user being 'authenticated', as well as cookie management for longer sessions. You need to add your own password checking logic. I'll probably want to replace this in the future, as I'm hashing my own passwords -- it looks like [FlaskSecurity](https://pythonhosted.org/Flask-Security/index.html) might be a good choice since it threads together a lot of lower level libraries. It also claims it provides easier OAuth integration, which might be good for some use cases.

First thing I did was to create a User class, inheriting both `db.Model` and flask-login's `UserMixIn`. The former gives me access to all the query convenience functions, and the latter implements [four methods](https://flask-login.readthedocs.io/en/latest/_modules/flask_login/mixins.html) to help flask-login. I also added in my own rudimentary hashing and password checking methods via `set_password` and `check_password`. It's important to note that flask-login doesn't actually seem to handle the checking of passwords, and it's something you need to do yourself. For example, if I didn't have the `user.check_password)` check below, nothing is stopping the user from being "logged in".

```python
user = User.query.filter_by(username=form.username.data).first()
if user and user.check_password(password=form.password.data):
    login_user(user)
```

From there, I created a `routes.py` file to hold all my app routes. At some point in the future, you can break out subdomains in your app into separate route files, like `blog_routes.py` or within a different directory, but I haven't yet. No need -- I'll only have 6 or 7 routes. The first thing I did was to initialize the plugin via `LoginManager()`. I also added that to my app factory and ran the `init_app` method. I also made a blueprint for the routes so I could set the decorator correctly. I don't want to import my `create_app` function to `routes.py` there, so I can create a blueprint then register it with the app in my `__init__`. Something like this:

```python
# routes.py
sf = flask.Blueprint('sf', __name__)

@sf.route('/login', methods=['GET', 'POST'])
def login():

# __init__.py
with app.app_context():
    # register blueprints
    app.register_blueprint(sf)
```

After that, I need to implement a few methods:
- `load_user`, with `@login_manager.userloader` as a decorator -> this is used by flask-login to load the user info on every page load.
- `login`, which will allow me to login a user
- `logout`, which, you guessed it, logs a user out
- `unauthorized`, with a `login_manager.unauthorized_handler`, which handles when a user tries to access a resource they are not allowed to access

Most of these methods are straightforward. The first thing I did was to create a `forms.py` file to handle the login form. I need to take user input and check it against the database to see if it's accurate. I used flask_wtf and wtforms for the task. The code was real simple.

Next was some basic html. First I made a base.html file which I will extend for various purposes. This saves a ton of code, of course, and keeps the HTML relatively modular. After base.html, I made a login.html, borrowing a bunch from all sorts of sources. One interesting thing that I found was the command `flask.flash` doesn't really do anything unless you get and display the messages. You need something like the below to display them.

{% raw %}
```html
{% for message in get_flashed_messages() %}
<div class="alert alert-warning">
  <button type="button" class="close" data-dismiss="alert">
    x
  </button>
  {{ message }}
</div>
{% endfor %}
```
{% endraw %}

The final piece of work was to set up an admin account. I set some variables in my environment to pull a username and password to create an admin account if it doesn't already exist. I wrote out a small function for it, and called it during the creation of my app. One interesting thing I couldn't figure out, however, was I was running into a null constraint violation. From everything I was reading, if you had a `db.Integer` column set as a primary key, you wouldn't need to pass a value into it for that integer to just auto-increment. That wasn't seeming to work for me, so I needed to pass in a value myself, like this: `user = User(id=1, username=username)`. There is only one admin user anyway, so this is fine. This will protect against the creation of any additional admin users, so it might actually be a feature, not a bug.

One other thing of note is that there is probably a design pattern to pull in data from a form, jsonify it, then pass that into my login (or any function that needs form info). This would allow me to decouple view from route/api logic. Routes shouldn't expect to be passed form data, but json objects. Nice to have for the future.

#### Admin edit view

### Final Takeaways
Flask allows a ton of customization, but you could probably be up and running faster with Django.

### Useful Commands
- `docker exec -it silentlyfailing bash` - start an interactive console in the docker container
- `heroku restart` - restarts your current heroku app, which is useful for odd errors
- `heroku logs --tail` - check the logs