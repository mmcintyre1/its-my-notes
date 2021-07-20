# Learning Notes Website

To run a local development server

    make server

To build the site

    make build

To update gems

    make update

In order to add a new path, you need to
- create the new folder location in the directory above website
- add the folder location to `docker-compose.yml`
- create a new top level file (like `books.md`, etc)
- add the path to `index.md`
- add the path to `_config.yml`
