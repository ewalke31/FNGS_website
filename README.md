# FNGS_website

## Tutorial

### Building Docker Container and Deploy Locally
```
git clone git@github.com:ebridge2/FNGS_website.git
cd FNGS_website
docker build -t <your-handle>/fngs .

# -v argument allows your container to use data that is only available locally. Ie, in this case, the data in
# /local/path/to/your/data/ would be visible inside the docker container at /data
docker run -ti -v /local/path/to/your/data/:/data --entrypoint /bin/bash <your-handle>/fngs
# takes you into the docker container
cd /ndmg/ndmg/scripts/
# runs the demo
./ndmg_demo-func.sh

# proceed to tutorial below about setting up the server
```

### Building Docker Container and Deploy on Web
```
git clone git@github.com:ebridge2/FNGS_website.git
cd FNGS_website
docker build -t <your-handle>/fngs .

# -v argument allows your container to use data that is only available locally. Ie, in this case, the data in
# /local/path/to/your/data/ would be visible inside the docker container at /data
docker run -ti -v /local/path/to/your/data/:/data -p portnum:portnum  --entrypoint /bin/bash <your-handle>/fngs
# takes you into the docker container
cd /ndmg/ndmg/scripts/
# runs the demo to make sure things work
./ndmg_demo-func.sh

# proceed to tutorial below about setting up the server
```

### Pulling Docker Container from Remote
```
docker pull ericw95/fngs:0.0.3

# -v argument allows your container to use data that is only available locally. Ie, in this case, the data in
# /local/path/to/your/data/ would be visible inside the docker container at /data
docker run -ti -v /local/path/to/your/data/:/data --entrypoint /bin/bash ericw95/fngs:0.0.3
# takes you into the docker container
cd /ndmg/ndmg/scripts/
./ndmg_demo-func.sh
# runs the demo

# proceed to tutorial below about setting up the server
```

### Local Setup Tutorial

Note that in order for this to work, you need to have FSL version 0.5.9 configured on your local machine (non-intuitive for non Red Head distributions). This path is not recommended. 

```
git clone -b nuisance-fmri git@github.com:neurodata/ndmg.git
cd ndmg/
python setup.py install
cd ndmg/scripts
# confirm that the pipeline runs without error
./ndmg_demo-func.sh

cd ../../../
git clone git@github.com:ebridge2/FNGS_website.git
cd FNGS_website/fngs
python manage.py runserver
# follow the link given to take you to the FNGS website. 


# proceed to tutorial below about setting up the server
```
