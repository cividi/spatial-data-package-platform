# gemeindescan-webui

# setup project

Create `var` folder in project root dir, in this folder the container data will be stored.
On linux you just can create the a normal folder. For Mac/Windows it's recommended to create a var folder
in the moby virtual maschine and make the host var folder a symlink to it (for better performence).

**for mac** (windows should be similar)

```bash
# enter moby
docker run --net=host --ipc=host --name=moby --uts=host --pid=host -it --security-opt=seccomp=unconfined --privileged --rm -v /:/host alpine ash"
# create var folder /host/var/lib/projects
mkdir -p /host/var/lib/projects/gemeindescan-webui
# exit moby, back to mac
ln -s /var/lib/projects/gemeindescan-webui var
``` 

**for linux**
```bash
mkdir var
```

regardless how you created the var folder you can now create the basic folder structure

```bash
docker run -it --rm -v `pwd`/var:/var/services busybox sh -c "mkdir -p /var/services/django; mkdir -p /var/services/postgres"
```

download containers and start them

```bash
. ./env.dev # load docker-compose.yml and docker-compose-dev.yml
docker-compose pull
make up
make init
```

# start docker containers

for dev, active 'COMPOSE_FILE' env var, only needs to be done once per working shell

```bash
. ./env.dev
```

`. .env.dev` set the env var `DOCKER_ENV` which you can add this to your `$PS1` command prompt to show if the enviroment is activated (optional). 
export DOCKER_ENV="(DEV)"

start containers

```bash
make up
```

## editor 

The project is setup to work with visual studio code as editor. Any other editor is also fine.
With vscode the plugins are automatically installed and linting and autocomplete works out of the box, 
with the data from inside the container. 

You need to start two editors with `code vue` and `code django` (install code command in path from vscode).
After they started you need to click on `reopen in container` (first time start takes a bit longer to install plugins). 

### vue vscode

Type `make` in the vscode terminal, that creates the node dev server on you maschine on the url [http://localhost:8080](http://localhost:8080)

### django vscode

Type `make` in the vscode terminal, that creates the django dev server on you maschine on the url [http://localhost:8081](http://localhost:8081)

# push to docker hub

- update the version number in the Makefiles in the docker folders and `docker-compose.yml`
- `make build` for all images in the root, or in the django or vue subfolders, this builds the docker images
- `make push` for all images in the root, or in the django or vue subfolders, this uploads the docker images to docker hub
