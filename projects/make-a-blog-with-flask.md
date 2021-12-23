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
