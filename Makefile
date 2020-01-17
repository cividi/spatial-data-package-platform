.PHONY: all

init:
	cd django && make init

up:
	docker-compose up -d

build:
	cd django && make build
	cd vue && make build

push:
	cd django && make push
	cd vue && make push

enter_django:
	cd django && make enter

enter_vue:
	cd vue && make enter

deploy_dev:
	cd vue && make build
	rsync -av --delete vue/dist $$DJANGO_DEV_HOST:$$DJANGO_DEV_PATH/var/vue/
	# ssh $$DJANGO_DEV_HOST ls $$DJANGO_DEV_PATH
