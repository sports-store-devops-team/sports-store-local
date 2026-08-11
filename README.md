# Sports Store Local Environment

Docker Compose orchestration for the polyrepo application. This repository must be beside `sports-store-frontend`, `sports-store-gateway`, and each of the five `sports-store-*-service` repositories in one parent directory.

## Setup and run

```sh
cp .env.example .env
docker compose build
docker compose up -d
docker compose ps
curl http://localhost:8080/health
```

On PowerShell, use `Copy-Item .env.example .env` instead of `cp`. The storefront is available at <http://localhost:8080>. Only the local-development Gateway publishes a host port; frontend, backends, and MongoDB remain on the internal Compose network. This adapter is not part of the AWS/EKS or Minikube request path and is not published to ECR.

Stop the stack without deleting MongoDB data:

```sh
docker compose down
```

Warning: `docker compose down -v` deletes the MongoDB volume and all locally persisted store data.

The `.env.example` values are development-only defaults. Replace them for any non-local environment and never commit `.env`.
