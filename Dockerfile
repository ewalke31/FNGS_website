FROM bids/base_fsl:5.0.9-3
MAINTAINER Eric Bridgeford <ericwb95@gmail.com>
RUN apt-get update && apt-get install -y python-dev python-setuptools python-numpy python-scipy zlib1g-dev python-nose fsl
RUN easy_install pip
RUN apt-get install -y libpng-dev libfreetype6-dev pkg-config
RUN pip install --ignore-installed cython numpy coveralls wget nibabel nilearn dipy sklearn networkx matplotlib==1.5.1 boto3 multiprocessing awscli Django==1.10.3
RUN apt-get install python-dateutil
RUN apt-get install -y zip unzip
RUN apt-get install -y vim git

RUN git clone -b eric-dev-merge2 https://github.com/neurodata/ndmg.git /ndmg && cd /ndmg && python setup.py install
RUN git clone https://github.com/ebridge2/FNGS_website /FNGS_website && mkdir /FNGS_server

# Get atlases
RUN mkdir /ndmg_atlases && wget -rnH --cut-dirs=3 --no-parent -P /ndmg_atlases http://openconnecto.me/mrdata/share/atlases/
#S3
RUN mkdir /.aws && printf "[default]\nregion = us-east-1" > /.aws/config
#ADD credentials.csv /credentials.csv
#RUN printf "[default]\naws_access_key_id = `tail -n 1 /credentials.csv | cut -d',' -f2`\naws_secret_access_key = `tail -n 1 /credentials.csv | cut -d',' -f3`" > /.aws/credentials && mv /.aws/  ${HOME} && rm /credentials.csv
#COPY version /version
ENTRYPOINT ["ndmg_bids"]


