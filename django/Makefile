GEMEINDESCAN_WEBUI_DJANGO=0.3.7
GEMEINDESCAN_WEBUI_DJANGO_PREV=0.3.6
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker-compose exec django")
all: dev run-tests run-tests-dev
.PHONY: all
default: dev

enter:
	$(DOCKER_EXEC) ash

build_docker:
	cd docker && DOCKER_BUILDKIT=1 docker build django \
	--cache-from smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO_PREV) \
	--build-arg BUILDKIT_INLINE_CACHE=1 \
	-t smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO)

push:
	docker push smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO)

dev:
	$(DOCKER_EXEC) uvicorn main.asgi:application --port 8081 --host 0.0.0.0 --reload

runprod:
	$(DOCKER_EXEC) uvicorn main.asgi:application --port 8081 --host 0.0.0.0

adminuser:
	$(DOCKER_EXEC) python3 manage.py createsuperuser

collectstatic:
	$(DOCKER_EXEC) python3 manage.py collectstatic --noinput

symlinks:
	$(DOCKER_EXEC) sh -c "cd /var/services/django; ln -s media downloads"

migrate:
	$(DOCKER_EXEC) python3 manage.py migrate
	make collectstatic

createcachetable:
	$(DOCKER_EXEC) python3 manage.py createcachetable

tests:
	$(DOCKER_EXEC) pytest --create-db

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
