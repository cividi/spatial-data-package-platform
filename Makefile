.PHONY: all

up:
	docker-compose up -d

build:
	cd fastapi && make build
	cd vue && make build

push:
	cd fastapi && make push
	cd vue && make push
