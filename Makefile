SHELL = /bin/zsh

test:
	echo "test"

test2:
	sudo docker-compose --env-file .env.dev stop  

test3:
	sudo docker-compose --env-file .env.dev up -d

test4:
 sudo docker-compose --env-file .env.dev up --build

test5:
	sudo docker-compose -f docker-compose.test.yml --env-file .env.test up --build
