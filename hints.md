## FNGS Website

database changes:

python manage.py makemigrations $APP

python manage.py migrate # reflect the changes


build the docker image (making sure the IP is in the allowed hosts before building)

```
docker build -t <your-handle>/fngs .
```

open the docker container with port forwarding on 8061
```
docker run -ti -p 8061:8061 --entrypoint /bin/bash ericw95/fngs
```
run the web service from inside the container
```
python manage.py runserver 0.0.0.0:8061
```
