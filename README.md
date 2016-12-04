# FNGS_website

## Tutorial

### Docker Tutorial
```
git clone git@github.com:ebridge2/FNGS_website.git
cd FNGS_website
docker build -t <your-handle>/fngs .

docker run -ti -v /local/path/to/your/data/:/data --entrypoint /bin/bash <your-handle>/fngs
# takes you into the docker container
cd /ndmg/ndmg/scripts/
./ndmg_demo-func.sh
# runs the demo
```

### Local Website Setup Tutorial

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
python setup.py runserver
# follow the link given to take you to the FNGS website. 
```
