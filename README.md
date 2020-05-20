# Gemeindescan Web UI

Web application under heavy development. For more information, please visit https://cividi.ch

The current tech stack of this project is:

- Vuetify
- Vue.js
- GraphQL
- Graphene
- Django
- Wagtail
- Docker

# Releases

*See [RELEASE.md](/RELEASE.md)*

# Developer guide

:construction:

For a tour of the app and a testing protocol see [`docs/testing.md`](/docs/testing.md).

## setup project

Add `www.local` and `django` to the 127.0.0.1 entry in `/etc/hosts` (for screenshot service).

```bash
touch env.hosts.prod # required file, can be empty and edited later
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

**start services**

```bash
# 1. shell
make start_vue
# 2. shell
make start_django
# 3. shell
make start_screenshotservice
```

You can also start the vue / django service from the vscode shell (see editor).

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

Type `make` in the vscode terminal, that creates the node dev server on you maschine on the url [http://localhost:8080](http://localhost:8080)

#### django vscode

Type `make` in the vscode terminal, that creates the django dev server on you maschine on the url [http://localhost:8081](http://localhost:8081)

## push to docker hub

- update the version number in the Makefiles in the docker folders and `docker-compose.yml`
- `make build` for all images in the root, or in the django or vue subfolders, this builds the docker images
- `make push` for all images in the root, or in the django or vue subfolders, this uploads the docker images to docker hub

## deploy

Type `make deploy_prod` in the project root. The file `env.hosts.prod` needs to have the right settings.

## additional docs

- [architecture](/docs/architecture.md)
- [django](/docs/django.md)
- [links](/docs/links.md)
- [grahpql](/docs/graphql.md)
- [troubleshooting](/docs/troubleshooting.md)
