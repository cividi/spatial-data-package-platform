# gemeindescan-webui

# start docker containers

for dev, active 'COMPOSE_FILE' env var, only needs to be done once per working shell

```bash
. ./env.dev
```

start containers

```bash
make up
```

# push to docker hub

- update the version number in the Makefiles in the docker folders and `docker-compose.yml`
- `make build` for all images in the root, or in the django or vue subfolders, this builds the docker images
- `make push` for all images in the root, or in the django or vue subfolders, this uploads the docker images to docker hub
