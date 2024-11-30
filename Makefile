.PHONY: help deploy start stop reset logs clean

export
DOCKER_PROJECT = ${PROJECT_NAME}

help:
	@echo "Available targets:"
	@echo "help	-	show this help message"
	@echo "deploy	-	Build & Up Docker Compose Services in Background"
	@echo "start	-	Build & Up Docker Compose Services"
	@echo "stop	-	Stop Docker Compose Services"
	@echo "reset	-	Stop & remove all Docker resources(volumes, images)"
	@echo "logs	-	Get logs live"
	@echo "clean	-	Clean all Dangling images"

deploy:
	docker compose -f docker-compose.yml up -d --build

start:
	docker compose -f docker-compose.yml up --build

stop:
	docker compose -f docker-compose.yml down

reset:
	docker compose -f docker-compose.yml down --volumes  --rmi all

logs:
	docker compose -f docker-compose.yml logs -f

clean:
	docker image prune
