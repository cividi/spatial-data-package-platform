DJANGO_VERSION=1.0.0-beta.2
DJANGO_VERSION_PREV=1.0.0-beta.1
NOTTY=$(shell command [ "$$DOCKER_NOTTY" = YES ] && echo "-T")
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker-compose exec $(NOTTY) django")
SHELL := /bin/bash

all: dev run-tests run-tests-dev
.PHONY: all
default: dev

enter:
	$(DOCKER_EXEC) ash

build_docker_gh:
	DOCKER_BUILDKIT=1 \
	docker buildx build \
		-t registry.gitlab.com/cividi/dfour/dfour-hub:latest \
		-t registry.gitlab.com/cividi/dfour/dfour-hub:$(DJANGO_VERSION_PREV) \
		--build-arg BUILDKIT_INLINE_CACHE=1 \
		--platform linux/amd64 \
		--cache-from ghcr.io/cividi/dfour-hub:$(DJANGO_VERSION) \
		--push \
		.

build_docker:
	cd docker && DOCKER_BUILDKIT=1 \
	docker buildx build \
		--build-arg BUILDKIT_INLINE_CACHE=1 \
		--cache-from smartuse/gemeindescan-webui-django:$(DJANGO_VERSION_PREV) \
		-t smartuse/gemeindescan-webui-django:$(DJANGO_VERSION) \
		--load \
		django

push:
	cd docker && DOCKER_BUILDKIT=1 \
	docker buildx build \
		--build-arg BUILDKIT_INLINE_CACHE=1 \
		--cache-from smartuse/gemeindescan-webui-django:$(DJANGO_VERSION_PREV) \
		-t smartuse/gemeindescan-webui-django:$(DJANGO_VERSION) \
		--platform linux/amd64,linux/arm64 \
		--push \
		django

dev:
	$(DOCKER_EXEC) uvicorn main.asgi:application --port 8081 --host 0.0.0.0 --reload

runprod:
	$(DOCKER_EXEC) uvicorn main.asgi:application --port 8081 --host 0.0.0.0

adminuser:
	$(DOCKER_EXEC) python3 manage.py createsuperuser

adminuser-noinput:
	$(DOCKER_EXEC) python3 manage.py createsuperuser --noinput --username admin --email admin@localhost.local

collectstatic:
	$(DOCKER_EXEC) python3 manage.py collectstatic --noinput

symlinks:
	$(DOCKER_EXEC) bash -c "mkdir -p /var/services/django/media && cd /var/services/django; [ ! -e /var/services/django/downloads ] && ln -s media downloads" || true

migrate:
	$(DOCKER_EXEC) python3 manage.py migrate
	make collectstatic

makemessages:
	$(DOCKER_EXEC) python3 manage.py makemessages --all

compilemessages:
	$(DOCKER_EXEC) python3 manage.py compilemessages

createcachetable:
	$(DOCKER_EXEC) python3 manage.py createcachetable

tests:
	$(DOCKER_EXEC) pytest --create-db -vvv

tests-dev:
	$(DOCKER_EXEC) pytest --reuse-db -vvv --nomigrations

delete-gemeinden-django:
	$(DOCKER_EXEC) python3 manage.py shell --command="from gsmap.models import Municipality;Municipality.objects.all().delete()"

import-gemeinden-json:
	$(DOCKER_EXEC) mkdir -p $(dir ./tmp/)
	$(DOCKER_EXEC) curl -o ./tmp/gemeinden.geojson -Ls https://datahub.io/n0rdlicht/ch-municipalities/r/2.geojson
	$(DOCKER_EXEC) python3 manage.py import-municipality ./tmp/gemeinden.geojson
	$(DOCKER_EXEC) rm ./tmp/gemeinden.geojson

init:
	make symlinks
	make migrate
	make createcachetable
	make adminuser
	make import-gemeinden-json

init-test:
	make symlinks
	make migrate
	make createcachetable
	make adminuser-noinput
	make import-gemeinden-json
