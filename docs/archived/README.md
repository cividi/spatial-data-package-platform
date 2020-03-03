# var folder

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

```bash
docker run -it --rm -v var-gemeindescan-webui:/var/services busybox sh -c "mkdir -p /var/services/django; mkdir -p /var/services/postgres"
```
