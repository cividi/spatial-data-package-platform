# gemeindescan-webui

## setup project

Create `var` folder in project root dir, in this folder the container data (database, generated files) will be stored.
On linux you just can create the a normal folder. For Mac/Windows it's recommended to create a var folder
in the moby virtual maschine and make the host var folder a symlink to it (for better performence, less permission problems).


**for linux**
```bash
mkdir var
```

**for mac**

```bash
# enter moby vm
docker run --net=host --ipc=host --name=moby --uts=host --pid=host -it --security-opt=seccomp=unconfined --privileged --rm -v /:/host alpine ash
# create var folder /host/var/lib/projects
mkdir -p /host/var/lib/projects/var-gemeindescan-webui
# exit moby, back to mac
exit
ln -s /var/lib/projects/var-gemeindescan-webui var
```

**windows**

```bash
# enter moby vm
docker run --net=host --ipc=host --name=moby --uts=host --pid=host -it --security-opt=seccomp=unconfined --privileged --rm -v /:/host alpine ash
# create var folder /host/var/lib/projects
mkdir -p /host/var/lib/projects/var-gemeindescan-webui
# go to your source code in moby mount '/host/host_mnt/c' is your c drive
cd /host/host_mnt/c/temp/gemeindescan-webui
ln -s /var/lib/projects/var-gemeindescan-webui var
# exit moby
exit
```

regardless how you created the var folder you can now create the basic folder structure

```bash
touch env.hosts.prod # required file, can be empty and edited later
docker run -it --rm -v `pwd`/var:/var/services busybox sh -c "mkdir -p /var/services/django; mkdir -p /var/services/postgres"
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
# exit django container
exit
# enter vue container
maker enter_vue
ln -s /node_modules ./
```

### start docker containers

```bash
make up
```

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

## additional docs

- [grahpql](/docs/graphql.md)
- [architecture](/docs/architecture.md)
