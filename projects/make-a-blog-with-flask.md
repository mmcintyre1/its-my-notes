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