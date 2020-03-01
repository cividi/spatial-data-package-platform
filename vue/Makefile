GEMEINDESCAN_WEBUI_VUE=0.3.0
DOCKER_VUE_NAME=$(shell basename $(shell dirname `pwd`))_vue_1
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -it $(DOCKER_VUE_NAME)")


.PHONY: all
default: dev

init:
	$(DOCKER_EXEC) ln -sf /node_modules ./

enter:
	$(DOCKER_EXEC) ash

build_docker:
	cd docker && DOCKER_BUILDKIT=1 docker build -t smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE) vue

push:
	docker push smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE)

dev:
	$(DOCKER_EXEC) yarn serve

build:
	$(DOCKER_EXEC) yarn build --mode production
	$(DOCKER_EXEC) cp -Ra dist /var/services/django/static/

build-dev-watch:
	$(DOCKER_EXEC) yarn build --mode development --watch

build-prod-watch:
	$(DOCKER_EXEC) yarn build --mode production --watch
