#!/bin/bash

# author: Seongwoo Lee Lukaid
# email: crescent3859@gmail.com

# This script is for running the prod server.

if [ "$1" == "bg" ]; then
    sudo docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d
elif [ "$1" == "build" ]; then
    sudo docker-compose -f docker-compose.prod.yml --env-file .env.prod up --build
elif [ "$1" == "stop" ]; then
    sudo docker-compose -f docker-compose.prod.yml --env-file .env.prod stop
else
    echo "Usage: ./run_prod.sh [bg|build|stop]"
fi