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

deploy_dev:
	cd vue && make build
	source env.hosts.prod && rsync -av --delete vue/dist $$DJANGO_DEV_HOST:$$DJANGO_DEV_PATH/var/vue/
	# ssh $$DJANGO_DEV_HOST make migrate
