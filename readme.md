# Four Hours Service

<div />

## Dependency

- docker, docker-compose
- nginx
- gunicorn
- django
- DRF
- postgresql
- firebase
- openai

## Installation \_ development

### in M1 mac add environment variable

```bash
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

### run

```bash
# in dev
sudo docker-compose -f docker-compose.dev.yml --env-file .env.dev up -d
```
