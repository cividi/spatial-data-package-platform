GEMEINDESCAN_WEBUI_FASTAPI=0.0.1

.PHONY: all

enter:
	$(DOCKER_EXEC) ash

build:
	cd docker && docker build -t smartuse/gemeindescan-webui-fastapi:$(GEMEINDESCAN_WEBUI_FASTAPI) fastapi

push:
	docker push smartuse/gemeindescan-webui-fastapi:$(GEMEINDESCAN_WEBUI_FASTAPI)
