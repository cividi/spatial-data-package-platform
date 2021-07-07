GEMEINDESCAN_WEBUI_VUE=0.3.9
GEMEINDESCAN_WEBUI_VUE_PREV=0.3.8
NOTTY=$(shell command [ "$$DOCKER_NOTTY" = YES ] && echo "-T")
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker-compose exec $(NOTTY) vue")


.PHONY: all
default: dev

enter:
	$(DOCKER_EXEC) ash

build_docker:
	cd docker && DOCKER_BUILDKIT=1 docker build vue \
	--cache-from smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE_PREV) \
	--build-arg BUILDKIT_INLINE_CACHE=1 \
	-t smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE)

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

build-dev-watch:
	$(DOCKER_EXEC) yarn build --mode development --watch

build-prod-watch:
	$(DOCKER_EXEC) yarn build --mode production --watch
