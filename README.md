## FNGS Website

database changes:

python manage.py makemigrations $APP

python manage.py migrate # reflect the changes


build the docker image

```
docker build -t <your-handle>/fngs .
```

open the docker container with port forwarding on 8060
```
docker run -ti -p 8061:8061 --entrypoint /bin/bash ericw95/fngs
```

