.PHONY: all

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
