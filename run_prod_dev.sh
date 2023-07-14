#!/bin/bash

# author: Seongwoo Lee Lukaid
# email: crescent3859@gmail.com

# This script is for running the prod server.

if [ "$1" == "bg" ]; then
    sudo docker-compose -f docker-compose.prod_dev.yml --env-file .env.prod up -d
elif [ "$1" == "build" ]; then
    sudo docker-compose -f docker-compose.prod_dev.yml --env-file .env.prod up --build
elif [ "$1" == "stop" ]; then
    sudo docker-compose -f docker-compose.prod_dev.yml --env-file .env.prod stop
elif [ "$1" == "exec" ]; then
    if [ "$2" == "makemigrations" ]; then
        sudo docker-compose -f docker-compose.prod_dev.yml --env-file .env.prod exec django python manage.py makemigrations
    elif [ "$2" == "migrate" ]; then
        sudo docker-compose -f docker-compose.prod_dev.yml --env-file .env.prod exec django python manage.py migrate
    fi
else
    echo "Usage: ./run_prod_dev.sh [bg|build|stop]"
fi

# exec
# sudo docker-compose -f docker-compose.dev.yml --env-file .env.dev exec django_prod python manage.py makemigrations
# sudo docker-compose -f docker-compose.dev.yml --env-file .env.dev exec django_prod python manage.py migrate