# VAMIKO project
*if requirements was updated rebuild image:*
docker build --rm -t muroslav/vamiko .
*go inside container*
docker exec -it reserv_django_1 /bin/sh
*push to dockerHUB*
docker tag 691b0984951b muroslav/vamiko
docker push muroslav/vamiko

*create db*
sudo apt-get install postgresql postgresql-contrib
sudo -i -u postgres
psql
CREATE DATABASE server_vamiko_postgres;
CREATE ROLE myroslav LOGIN;
CREATE USER davide WITH PASSWORD 'jw8s0F4';
\q