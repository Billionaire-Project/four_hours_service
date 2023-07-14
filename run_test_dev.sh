#!/bin/bash

# author: Seongwoo Lee Lukaid
# email: crescent3859@gmail.com

# This script is for running the development server.

if [ "$1" == "bg" ]; then
    sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test up -d
elif [ "$1" == "build" ]; then
    sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test up --build
elif [ "$1" == "stop" ]; then
    sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test stop
elif [ "$1" == "exec" ]; then
    if [ "$2" == "makemigrations" ]; then
        sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test exec django python manage.py makemigrations
    elif [ "$2" == "migrate" ]; then
        sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test exec django python manage.py migrate
    fi
else
    echo "Usage: ./run_dev.sh [bg|build|stop]"
fi

# exec
# sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test exec django python manage.py makemigrations
# sudo docker-compose -f docker-compose.test_dev.yml --env-file .env.test exec django python manage.py migrate