#!/bin/bash

# author: Seongwoo Lee Lukaid
# email: crescent3859@gmail.com

# This script is for running the test server.

if [ "$1" == "bg" ]; then
    sudo docker-compose -f docker-compose.test.yml --env-file .env.test up -d
elif [ "$1" == "build" ]; then
    sudo docker-compose -f docker-compose.test.yml --env-file .env.test up --build
elif [ "$1" == "stop" ]; then
    sudo docker-compose -f docker-compose.test.yml --env-file .env.test stop
else
    echo "Usage: ./run_test.sh [bg|build|stop]"
fi