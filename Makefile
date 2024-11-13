SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

.PHONY: build clean coverage createssl key phpunit-copy seed shell start stop terminal test

build:
> COMPOSE_DOCKER_CLI_BUILD=1 docker compose up --force-recreate --build

clean:
> docker compose down
> docker compose rm

shell:
> docker compose exec learning-py-app bash

terminal: shell

start:
> docker compose up

stop:
> docker compose down

createssl:
> rm -rf .docker/conf/certs
> mkdir .docker/conf/certs
> openssl req -x509 -nodes -new -sha256 -days 1024 -newkey rsa:2048 -keyout .docker/conf/certs/learning-py.com.key -out .docker/conf/certs/learning-py.com.pem -subj "/C=US/ST=NewYork/L=NewYork/O=IQVIA/CN=learning-py.com"
> openssl x509 -outform pem -in .docker/conf/certs/learning-py.com.pem -out .docker/conf/certs/learning-py.com.crt
