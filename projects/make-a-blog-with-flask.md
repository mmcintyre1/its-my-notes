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
- Netlify (hosting)
- TBD (data layer hosting)

## Repository
https://github.com/mmcintyre1/silently-failing


## Starting out - Day 1
I think my first step is going to be getting a simple Flask app functioning in a docker container, then deploying that to Netlify. If I can start with the CI/CD so I can easily push changes live, it'll allow me to concentrate on the stuff I know less well -- presentation. The last app I hosted on Netlify was a jekyll app, so there was no data layer. Doesn't seem like netlify offers any database services, but I can probably find something easy enough.

### Making the Repository and a Simple Flask App
All right, step 1 is making a repository structure for the Flask app. Flask recommends [this structure](https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/), so that's what I've gone with. I've got the project structure in [this commit](https://github.com/mmcintyre1/silently-failing/tree/b702777d1307d8c8362d45dd39e5754c7ff69b6d). I made `templates` and `static` folder as well, but they are empty so won't be committed yet.

I've created a virtual environment by using the command `python -m venv venv` and then running `pip install flask`.

I can run this locally easily enough. First I run `export FLASK_APP=silently-failing`, then I run `flask run`. This will get me up and running locally. Looks like shit, but you have to start somewhere.

### Getting Docker and Docker Desktop with WSL2
Since I'm running in WSL2, I'm using Docker Desktop to make my life easier. I could probably run docker directly in WSL2, but Docker and Windows make that really silly. There's a pretty good rundown of [Docker's integration with WSL2](https://www.docker.com/blog/new-docker-desktop-wsl2-backend/).

I used the Windows docs for [getting started with Docker and WSL2](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers). As a side note, Microsoft's documentation is normally exceptional. They have really upped their game.

### Doing the Docker thing
So now I need to build the docker container image, then run that container image. We can write out the instructions for building that container image in a `Dockerfile`, then we can build the container image via `docker build` then we can run that container via `docker run`. I'm following [Docker's guide](https://docs.docker.com/language/python/build-images/). [This](https://github.com/mmcintyre1/silently-failing/blob/afe7e4d3bfc4d1e3c550a4a8319b292dd441dd9f/Dockerfile) is what my `Dockerfile` looks like right now.

Now I can build the image using the command `docker build --tag silently-failing .` while in my applications root directory. Giving the image a name will make it easier to run commands later. The tag is in the format of `name:tag`, and leaving off the tag omits it from the image.

Then, I can run the image container via `docker run -d -p 5000:5000 silently-failing`.
- `-d` means in detached mode, so it runs in the background
- `-p` publishes the ports within the container to outside the container
- `silently-failing` tells it what image to run.

#### Difference Between `CMD` and `ENTRYPOINT`
I've written my `Dockerfile` with `CMD`, but I've seen `ENTRYPOINT` used as well. [Here's](https://www.bmc.com/blogs/docker-cmd-vs-entrypoint/#) a pretty decent resource on the topic, but it seems to boil down to whether or not you want your commands to be able to overridden at the command line when starting the image. Your `Dockerfile` needs either a `CMD` or an `ENTRYPOINT`. I'm using the command `python3 -m flask run --host=0.0.0.0`, but if I wanted to use `python3 -m flask shell`, I can do that easily by running the command `docker run silently-failing flask shell`.

### Adding in Gunicorn
So now I want to add in a web server to replace the simple one Flask gives. The web server just needs to implement WSGI and will integrate with Flask as Flask is expecting WSGI. The [wikipedia for WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) is a pretty good resource for more information. Need to update the Dockerfile. I'm loosely using [this](https://itnext.io/setup-flask-project-using-docker-and-gunicorn-4dcaaa829620) as a resource, but instead of using a shell script I'll just pass in the start up commands via `CMD`. [This](https://github.com/mmcintyre1/silently-failing/blob/365d3c739f4c0fae2d3686728718bc709481a760/Dockerfile) is what my `Dockerfile` looks like now.

Another thing I've noticed is that in working with docker, I am running `docker build` a bunch, and I have a ton of images I need to go through and delete. This is easy enough via Docker Desktop, but surely there is a better way to manage the lifecycle of these containers and clean up detritus.

### Simplifying Management with Docker compose

### Making Makefiles
