include .env
SHELL := /bin/bash

psql: docker compose exec db psql -U postgres

docker-build:
    source .env
    docker compose --env-file .env build --no-cache

docker-up:
    source .env
    docker compose --env-file .env up -d

docker-down:
    docker compose down