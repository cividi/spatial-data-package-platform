# Troubleshooting

## init

If you want/need a clean state you can delete the var docker volume.
`docker volume rm var-gemeindescan-webui`

## vscode

If you have a vscode related problem it could help to delete the vscode docker volume.
- django: `docker volume rm gemeindescan-webui_vscode-remote-django`
- vue: `docker volume rm gemeindescan-webui_vscode-remote-vue`

## windows

### django

When the `./manage.py` doesn't work your need to execute `python3 manage.py` instead.

## docker

Do a `docker-compose kill` and `docker-compose rm` if there are some container problems.

With `docker-compose logs -f` you can see the output of the containers if there is a problem.

### docker cleanup

With `docker images` you can list all download images and display the hash image id.
Do `docker rmi 2dadea35c9d0 8ae2cb92062c ...` to delete not needed images and free up some space.
