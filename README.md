# FNGS_website

# Tutorial

## Getting the Pipeline Running

### Building Docker Container for Pipeline use Only
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
```

### Building Docker Container for Web Use

Note that this guide is very similar to the preceeding guide, except now we need to forward ports when we use the docker container.
```
git clone git@github.com:ebridge2/FNGS_website.git
cd FNGS_website
docker build -t <your-handle>/fngs .

# -v argument allows your container to use data that is only available locally. Ie, in this case, the data in
# /local/path/to/your/data/ would be visible inside the docker container at /data
docker run -ti -v /local/path/to/your/data/:/data -p <portnum>:<portnum>  --entrypoint /bin/bash <your-handle>/fngs
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

Note that in order for this to work, you need to have FSL version 0.5.9 configured on your local machine (non-intuitive for non Red Hat distributions). This path is not recommended unless you have experience installing FSL on non-RH Linux distributions. 

```
git clone -b nuisance-fmri git@github.com:neurodata/ndmg.git
cd ndmg/
python setup.py install
cd ndmg/scripts
# confirm that the pipeline runs without error
./ndmg_demo-func.sh

cd ../../../
git clone git@github.com:ebridge2/FNGS_website.git

# proceed to tutorial below about setting up the server
```

## Server Tutorial

Now that we have the pipeline working, we can try to get some scans uploaded and analyzed for visualization and downloading through the web service. From inside the docker container (or, if you installed locally, from the website folder):
```
$ cd /FNGS_website/fngs # (if installed locally, cd FNGS_website/fngs from wherver the FNGS_website repo is cloned)
$ python manage.py runserver 0.0.0.0:<portnum> # puts the server up on 0.0.0.0:<portnum> for whatever port you choose
Performing system checks...

System check identified some issues:

WARNINGS:
?: (urls.W001) Your URL pattern '^$' uses include with a regex ending with a '$'. Remove the dollar from the regex to avoid problems including URLs.

System check identified 1 issue (0 silenced).
December 07, 2016 - 20:33:52
Django version 1.10.4, using settings 'fngs.settings'
Starting development server at http://localhost:8000/ # this line tells you where to go to open the service, or just click
Quit the server with CONTROL-C.
```
Following the link given by the service will take you to the home page:
![FNGS Homepage](https://cloud.githubusercontent.com/assets/8883547/20985816/12fabc48-bc94-11e6-90d8-d74aa0e1bf70.png)

