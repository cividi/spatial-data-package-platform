SHELL = /bin/bash
DOCKER_EXEC_DJANGO=$(shell command -v docker > /dev/null && echo "docker-compose exec django")
DOCKER_EXEC_VUE=$(shell command -v docker > /dev/null && echo "docker-compose exec vue")
DOCKER_EXEC_WWW=$(shell command -v docker > /dev/null && echo "docker-compose exec www")

DOCKER_CRON_VUE=$(shell command -v docker > /dev/null && echo "docker-compose exec -T vue")
DOCKER_CRON_DJANGO=$(shell command -v docker > /dev/null && echo "docker-compose exec -T django")

APP_VERSION=$(shell git describe --tags)

.PHONY: tests

init:
	cd django && make init
	cd vue && make init

up:
	export APP_VERSION=$(APP_VERSION) && docker-compose up -d

down: stop

stop:
	docker-compose stop

build_docker:
	cd django && make build_docker
	cd vue && make build_docker

build: build_docker

push:
	cd django && make push
	cd vue && make push

enter_django:
	$(DOCKER_EXEC_DJANGO) ash

enter_vue:
	$(DOCKER_EXEC_VUE) ash

enter_www:
	$(DOCKER_EXEC_WWW) ash

start_all: up
	$(DOCKER_CRON_VUE) make &
	$(DOCKER_CRON_DJANGO) make &
	$(DOCKER_CRON_VUE) make screenshotservice &

start_vue:
	$(DOCKER_EXEC_VUE) make

start_django:
	$(DOCKER_EXEC_DJANGO) make

start_screenshotservice:
	$(DOCKER_EXEC_VUE) make screenshotservice

reload_www:
	$(DOCKER_EXEC_WWW) sh -c 'openresty -t & openresty -s reload'


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

deploy_local:
	export APP_VERSION=$(APP_VERSION) && docker-compose up -d
	make -f vue/Makefile build-cron
	docker-compose exec -T vue rsync -av --delete dist/ /var/services/django/static/dist/
	docker-compose exec -T django make migrate
	docker-compose exec -T django killall -TERM gunicorn
	docker-compose exec -T vue killall -TERM node

slack-push:
	source env.hosts.prod && test -v SLACK_APP_HOOK && curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$$SLACK_APP_TEXT\"}" "https://hooks.slack.com/services/$$SLACK_APP_HOOK"

update:
	make deploy_local && make slack-push; exit 0

ab-graphql:
	ab -p tests/graphql-autocomplete-post.json -T application/json -c 10 -n 2000 http://gemeindescan.ch/graphql/

ab-html:
	ab -c 10 -n 2000 http://gemeindescan.ch/

dump-db:
	@docker-compose exec pdb sh -c 'pg_dump --no-owner --no-acl --schema=public -U $$POSTGRES_USER $$POSTGRES_DB' > tmp/dump.sql

import-db:
	@docker-compose exec pdb sh -c 'psql -U $$POSTGRES_USER $$POSTGRES_DB < /var/services/postgres/var/dump.sql'

tests:
	cd django && make tests
	cd vue && make tests
