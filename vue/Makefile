GEMEINDESCAN_WEBUI_VUE=0.3.4
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

build:
	$(DOCKER_EXEC) yarn build --mode production
	$(DOCKER_EXEC) rsync -av --delete dist /var/services/django/static/

build-cron:
	$(DOCKER_EXEC_CRON) yarn build --mode production
	$(DOCKER_EXEC_CRON) rsync -av --delete dist /var/services/django/static/

build-dev-watch:
	$(DOCKER_EXEC) yarn build --mode development --watch

build-prod-watch:
	$(DOCKER_EXEC) yarn build --mode production --watch
