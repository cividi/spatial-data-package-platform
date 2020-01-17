GEMEINDESCAN_WEBUI_DJANGO=0.0.1
DOCKER_DJANGO_NAME=$(shell basename $(shell dirname `pwd`))_django_1
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -it $(DOCKER_DJANGO_NAME)")

.PHONY: all

enter:
	$(DOCKER_EXEC) ash

build:
	cd docker && docker build -t smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO) django

push:
	docker push smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO)

run:
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

init:
	make migrate
	make adminuser
