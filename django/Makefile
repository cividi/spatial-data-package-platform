GEMEINDESCAN_WEBUI_DJANGO=0.0.1
DOCKER_DJANGO_NAME=$(shell basename $(shell dirname `pwd`))_django_1
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -it $(DOCKER_DJANGO_NAME)")

.PHONY: all
default: dev

enter:
	$(DOCKER_EXEC) ash

build:
	cd docker && docker build -t smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO) django

push:
	docker push smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO)

dev:
	$(DOCKER_EXEC) uvicorn main.asgi:application --port 8081 --host 0.0.0.0 --reload

runprod:
	$(DOCKER_EXEC) uvicorn main.asgi:application --port 8081 --host 0.0.0.0


adminuser:
	$(DOCKER_EXEC) ./manage.py createsuperuser

collectstatic:
	$(DOCKER_EXEC) ./manage.py collectstatic --noinput

migrate:
	$(DOCKER_EXEC) ./manage.py migrate
	make collectstatic

import-gemeinden-json:
	jq '[.[]|{ "model": "gsmap.municipality", pk: .gemeinde.BFS_NUMMER, "fields": { name: .gemeinde.NAME, canton: .kanton.KUERZEL }}]' tmp/gemeinden.json | ./manage.py loaddata --format=json -

init:
	# docker run -it --rm -v `pwd`/var:/var/services busybox sh -c "mkdir -p /var/services/django"
	make migrate
	make adminuser
