# VAMIKO project
*if requirements was updated rebuild image:*
docker build --rm -t muroslav/vamiko .
*go inside container*
docker exec -it reserv_django_1 /bin/sh
*push to dockerHUB*
docker tag 691b0984951b muroslav/vamiko
docker push muroslav/vamiko

python manage.py createsuperuser