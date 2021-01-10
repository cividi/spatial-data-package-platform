# Gemeindescan Web

A web application for publishing and collaborating around urban planning projects. This project is part of the  [Cividi](https://cividi.ch) solution for holistic urban assessments, used as a tool for setting planning priorities.

For more information, please visit [Gemeindescan.ch](https://gemeindescan.ch) and read our [Whitepaper](https://bitbucket.org/cividi/whitepaper).

# Additional documentation

- [Release notes](./RELEASE.md)
- [Architecture](./docs/architecture.md)
- [Troubleshooting](./docs/troubleshooting.md)
- [Test guide](./docs/testing.md)
- [Django](./docs/django.md)
- [GraphQL](./docs/graphql.md)
- [Further links](./docs/links.md)

# Developer guide

:construction: The current tech stack of this project is:

- Vuetify
- Vue.js
- GraphQL
- Graphene
- Django
- Wagtail
- Docker

For a tour of the app and a testing protocol see [`docs/testing.md`](./docs/testing.md).

## setup project

Add `www.local` and `django` to the 127.0.0.1 entry in `/etc/hosts` (for screenshot service).

```bash
touch env.hosts.prod # required file, can be empty and edited later
cp etc/nginx/www.local.dev etc/nginx/www.local.conf # default www.local.conf is not under version control
```

download containers and start them

```bash
docker-compose pull
make up
make init
```

if `make init` doesn't work you can execute the commands one by one.

```bash
# go into django container
make enter_django
cd django
python3 manage.py migrate
python3 manage.py createsuperuser
make import-gemeinden-json
# exit django container
exit
# enter vue container
maker enter_vue
ln -s /node_modules ./
```

For development we use a named docker volume for the `var` folder inside the container, this named
volume will be created automatically. This makes setup under windows easier.
For production under linux a bind mount is used, for easier backups and no accidental data deletion.

Database files and static generated files are stored in `var` folder.

### start docker containers

```bash
make up
```

The front- and backend should now be accessible via

```
Frontend: http://www:8000
Backend:  http://www:8000/gmanage
GraphQLi: http://www:8000/graphql
```

**start services**

Start all the services at the same time using

```bash
make start_all
```

or individually using:

```bash
# 1. shell
make start_vue
# 2. shell
make start_django
# 3. shell
make start_screenshotservice
```

You can also start the vue / django service from the vscode shell (see editor).

**stop services**

```bash
make stop
```

### tests

```bash
make tests
```

This command runs first the backend tests and afterwards the frontend test.

For the backend tests a new test database is generated and the fixtures are loaded.


### editor

The project is setup to work with visual studio code as editor. Any other editor is also fine.
With vscode the plugins are automatically installed and linting and autocomplete works out of the box,
with the data from inside the container.

You need to have installed the vscode extension `Remote - Containers` in your local vscode installation.

You need to start two editors with `code vue` and `code django` (install code command in path from vscode).
After they started you need to click on `reopen in container` (first time start takes a bit longer to install plugins).

#### vue vscode

Type `make` in the vscode terminal, that creates the node dev server on your maschine which is accessible via [http://www:8000](http://www:8000). Make sure to add `www` and `www.local` to your `/etc/hosts` file to point to `127.0.0.1`.

#### django vscode

Type `make` in the vscode terminal, that creates the django dev server on your maschine on the url [http://www:8000/gmanage](http://www:8000/gmanage).

## push to docker hub

- update the version number in the Makefiles in the docker folders and `docker-compose.yml`
- `make build` for all images in the root, or in the django or vue subfolders, this builds the docker images
- `make push` for all images in the root, or in the django or vue subfolders, this uploads the docker images to docker hub

## deploy

Type `make deploy_prod` in the project root. The file `env.hosts.prod` needs to have the right settings.
