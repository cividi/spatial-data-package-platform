SHELL = /bin/bash
NOTTY=$(shell command [ "$$DOCKER_NOTTY" = YES ] && echo "-T")
DOCKER_EXEC_DJANGO=$(shell command -v docker > /dev/null && echo "docker-compose exec $(NOTTY) django")
DOCKER_EXEC_VUE=$(shell command -v docker > /dev/null && echo "docker-compose exec $(NOTTY) vue")
DOCKER_EXEC_WWW=$(shell command -v docker > /dev/null && echo "docker-compose exec $(NOTTY) www")


.PHONY: deploy_version

init:
	cd django && make init

init-test:
	sleep 10 # wait for db setup
	cd django && make init-test

up:
	docker-compose up -d

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
	$(DOCKER_EXEC_WWW) bash

start_all: up
	$(DOCKER_VUE) $(NOTTY) make &
	$(DOCKER_DJANGO) $(NOTTY) make &
	$(DOCKER_VUE) make screenshotservice &

start_vue:
	$(DOCKER_EXEC_VUE) make

start_django:
	$(DOCKER_EXEC_DJANGO) make

start_screenshotservice:
	$(DOCKER_EXEC_VUE) make screenshotservice

reload_www:
	$(DOCKER_EXEC_WWW) sh -c 'openresty -t & openresty -s reload'

deploy_local:
	docker-compose up -d
	DOCKER_NOTTY=YES make -f vue/Makefile build
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

deploy_version:
	bash -c 'printf "%s\t%s" "$$(git describe --abbrev=0 --tags)" "$$(git rev-parse --short HEAD)" > django/VERSION'
	cp django/VERSION vue/VERSION

-include deploy_version
