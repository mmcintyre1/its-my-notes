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
All right, step 1 is making a repository structure for the Flask app. Flask recommends this structure defined [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/), so that's what I've gone with. I've got the project structure in [this commit](https://github.com/mmcintyre1/silently-failing/tree/b702777d1307d8c8362d45dd39e5754c7ff69b6d). I made `templates` and `static` folder as well, but they are empty so won't be committed yet.

I've created a virtual environment by using the command `python -m venv venv` and then running `pip install flask`.

I can run this locally easily enough. First I run `export FLASK_APP=silently-failing`, then I run `flask run`. This will get me up and running locally. Looks like shit, but we are up and running.

###