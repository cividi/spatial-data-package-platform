.PHONY: all

up:
	docker-compose up -d

build:
	cd fastapi && make build
	cd vue && make build

push:
	cd fastapi && make push
	cd vue && make push

enter_fastapi:
	cd fastapi && make enter

enter_vue:
	cd vue && make enter
