FROM bids/base_fsl:5.0.9-3
MAINTAINER Eric Bridgeford <ericwb95@gmail.com>
RUN apt-get update && apt-get install -y python-dev python-setuptools python-numpy python-scipy zlib1g-dev python-nose fsl
RUN easy_install pip
RUN apt-get install -y libpng-dev libfreetype6-dev pkg-config
RUN pip install --ignore-installed cython numpy coveralls wget nibabel nilearn dipy sklearn networkx boto3 multiprocessing awscli
RUN pip install django
RUN pip install matplotlib==1.5.1
RUN apt-get install python-dateutil
RUN apt-get install -y zip unzip
RUN apt-get install -y vim git
RUN git clone -b nuisance-fmri https://github.com/neurodata/ndmg.git /ndmg && cd /ndmg && python setup.py install
# apparently matplotlib gets messed up during install of ndmg
RUN pip install -U --force-reinstall matplotlib==1.5.1

# clone the website repo and make the location for the downloads
RUN git clone https://github.com/ebridge2/FNGS_website.git && mkdir /FNGS_server && mkdir /FNGS_server/input_data && mkdir /FNGS_server/output_data

RUN cd /FNGS_website/fngs && python manage.py makemigrations analyze && python manage.py migrate

# Get atlases
RUN cd /FNGS_server && wget http://openconnecto.me/mrdata/share/demo_data/less_small_atlases.zip && unzip less_small_atlases.zip && mv demo_atlases atlases
RUN mkdir /ndmg_atlases && wget -rnH --cut-dirs=3 --no-parent -P /ndmg_atlases http://openconnecto.me/mrdata/share/atlases/
#S3
#RUN mkdir /.aws && printf "[default]\nregion = us-east-1" > /.aws/config
#ADD credentials.csv /credentials.csv
#RUN printf "[default]\naws_access_key_id = `tail -n 1 /credentials.csv | cut -d',' -f2`\naws_secret_access_key = `tail -n 1 /credentials.csv | cut -d',' -f3`" > /.aws/credentials && mv /.aws/  ${HOME} && rm /credentials.csv
#COPY version /version
ENTRYPOINT ["ndmg_bids"]
