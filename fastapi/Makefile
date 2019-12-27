GEMEINDESCAN_WEBUI_FASTAPI=0.0.2
DOCKER_FASTAPI_NAME=$(shell basename $(shell dirname `pwd`))_fastapi_1
DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -it $(DOCKER_FASTAPI_NAME)")

.PHONY: all

enter:
	$(DOCKER_EXEC) ash

build:
	cd docker && docker build -t smartuse/gemeindescan-webui-fastapi:$(GEMEINDESCAN_WEBUI_FASTAPI) fastapi

push:
	docker push smartuse/gemeindescan-webui-fastapi:$(GEMEINDESCAN_WEBUI_FASTAPI)

run:
	$(DOCKER_EXEC) uvicorn main:app --port 8081 --host 0.0.0.0 --reload
