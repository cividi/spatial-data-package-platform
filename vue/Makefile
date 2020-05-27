GEMEINDESCAN_WEBUI_VUE=0.3.5
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker-compose exec vue")
DOCKER_EXEC_CRON=$(shell command -v docker > /dev/null && echo "docker-compose exec -T vue")


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

screenshotservice:
	$(DOCKER_EXEC) node /opt/vue/screenshot-service/screenshot-server.js

tests:
	$(DOCKER_EXEC) yarn test

build:
	$(DOCKER_EXEC) yarn build --mode production

build-cron:
	$(DOCKER_EXEC_CRON) yarn build --mode production

build-dev-watch:
	$(DOCKER_EXEC) yarn build --mode development --watch

build-prod-watch:
	$(DOCKER_EXEC) yarn build --mode production --watch
