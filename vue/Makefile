GEMEINDESCAN_WEBUI_VUE=0.0.1
DOCKER_VUE_NAME=$(shell basename $(shell dirname `pwd`))_vue_1
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -it $(DOCKER_VUE_NAME)")


.PHONY: all

enter:
	$(DOCKER_EXEC) ash

build_docker:
	cp yarn.lock package.json docker/vue/
	cd docker && docker build -t smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE) vue
	rm docker/vue/yarn.lock docker/vue/package.json

push:
	docker push smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE)

dev:
	yarn serve

build:
	yarn build

build-dev-watch:
	yarn build --mode development --watch

build-prod-watch:
	yarn build --mode production --watch
