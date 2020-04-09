SHELL = /bin/bash

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

deploy_local:
	docker-compose up -d
	make -f vue/Makefile build
	source env.hosts.prod && rsync -av --delete vue/dist $$VUE_LOCAL_PATH
	docker-compose exec django make migrate
	docker-compose exec django killall -TERM gunicorn

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
