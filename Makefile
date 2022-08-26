COMPOSE = docker-compose
FILE = docker-compose.yml
APP = itsmynotes

# Non file-generating targets
.PHONY: build server kill

h help:
	@grep '^[a-z]' Makefile

build:
	$(COMPOSE) -f "$(FILE)" build $(services) -p $(APP)

s server:
	$(COMPOSE) -p $(APP) up -d

k kill:
	$(COMPOSE) -p $(APP) down