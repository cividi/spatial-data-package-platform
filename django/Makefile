GEMEINDESCAN_WEBUI_DJANGO=0.3.0
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker-compose exec django")

.PHONY: all
default: dev

enter:
	$(DOCKER_EXEC) ash

build_docker:
	cd docker && docker build -t smartuse/gemeindescan-webui-django:$(GEMEINDESCAN_WEBUI_DJANGO) django

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

migrate:
	$(DOCKER_EXEC) python3 manage.py migrate
	make collectstatic

delete-gemeinden-django:
	$(DOCKER_EXEC) python3 manage.py shell --command="from gsmap.models import Municipality;Municipality.objects.all().delete()"

import-gemeinden-json:
	$(DOCKER_EXEC) sh -c "curl -Ls https://datahub.io/n0rdlicht/ch-municipalities/r/0.json | jq '[.[]|{ \"model\": \"gsmap.municipality\", pk: .gemeinde.BFS_NUMMER, \"fields\": { name: .gemeinde.NAME, canton: .kanton.KUERZEL }}]' | python3 manage.py loaddata --format=json -"

init:
	make migrate
	make adminuser
	make import-gemeinden-json
