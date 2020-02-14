.PHONY: all

init:
	cd django && make init
	cd vue && make init

up:
	docker-compose up -d

build_docker:
	cd django && make build_docker
	cd vue && make build_docker

push:
	cd django && make push
	cd vue && make push

enter_django:
	cd django && make enter

enter_vue:
	cd vue && make enter

deploy_prod:
	cd vue && make build
	source env.hosts.prod && ssh $$DJANGO_PROD_HOST -t "cd $$DJANGO_PROD_PATH && git pull -v"
	source env.hosts.prod && ssh $$DJANGO_PROD_HOST -t "cd $$DJANGO_PROD_PATH && COMPOSE_FILE=$$COMPOSE_PROD docker-compose up -d"
	source env.hosts.prod && rsync -av --delete vue/dist $$DJANGO_PROD_HOST:$$VUE_PROD_PATH
	source env.hosts.prod && ssh $$DJANGO_PROD_HOST -t "cd $$DJANGO_PROD_PATH && COMPOSE_FILE=$$COMPOSE_PROD docker-compose exec django make migrate"
	source env.hosts.prod && ssh $$DJANGO_PROD_HOST -t "cd $$DJANGO_PROD_PATH && COMPOSE_FILE=$$COMPOSE_PROD docker-compose exec django killall -TERM gunicorn"

deploy_dev:
	cd vue && make build
	source env.hosts.prod && ssh $$DJANGO_DEV_HOST -t "cd $$DJANGO_DEV_PATH && git pull -v"
	source env.hosts.prod && ssh $$DJANGO_DEV_HOST -t "cd $$DJANGO_DEV_PATH && COMPOSE_FILE=$$COMPOSE_DEV docker-compose up -d"
	source env.hosts.prod && rsync -av --delete vue/dist $$DJANGO_DEV_HOST:$$VUE_DEV_PATH
	source env.hosts.prod && ssh $$DJANGO_DEV_HOST -t "cd $$DJANGO_DEV_PATH && COMPOSE_FILE=$$COMPOSE_DEV docker-compose exec django make migrate"
	source env.hosts.prod && ssh $$DJANGO_DEV_HOST -t "cd $$DJANGO_DEV_PATH && COMPOSE_FILE=$$COMPOSE_DEV docker-compose exec django killall -TERM gunicorn"

ab-graphql:
	ab -p tests/graphql-autocomplete-post.json -T application/json -c 10 -n 2000 http://gemeindescan.ch/graphql/

ab-html:
	ab -c 10 -n 2000 http://gemeindescan.ch/
