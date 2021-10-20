Nginx configuration
---

We are currently using a mostly out-of-the-box Docker image for the web server (www in Docker Compose).

The specific image used is https://hub.docker.com/u/openresty

All the files in this directory are available at `/etc/nginx/conf.d` on the container. Here are some notes on how this is set up.

Self signed certificates for SSL in development are generated using the configuration in `localhost.request` and these commands:

```
docker-compose run www bash
cd /etc/nginx/conf.d
apk add openssl
openssl req -batch -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -config localhost.request
exit
```
