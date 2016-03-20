# VAMIKO project
*if requirements was updated rebuild image:*
docker build --rm -t vamiko/project .
*go inside container*
docker exec -it visareserv_django_1 /bin/sh
*push to dockerHUB*
docker tag 691b0984951b muroslav/vamiko
docker push muroslav/vamiko
