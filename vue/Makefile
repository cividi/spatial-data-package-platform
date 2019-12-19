GEMEINDESCAN_WEBUI_VUE=0.0.1

.PHONY: all

enter:
	$(DOCKER_EXEC) ash

build:
	cd docker && docker build -t smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE) vue

push:
	docker push smartuse/gemeindescan-webui-vue:$(GEMEINDESCAN_WEBUI_VUE)
