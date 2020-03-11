
FROM gcr.io/cloud-datalab/datalab:latest

# update GCP
RUN gcloud components update

# gdal
RUN echo "deb http://ppa.launchpad.net/ubuntugis/ppa/ubuntu xenial main" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y gdal-bin 

# Install Earth Engine Python API dependencies.
RUN apt-get update \
  && apt-get install -y build-essential libssl-dev libffi-dev \
  && pip install cryptography \
  && apt-get purge -y build-essential libssl-dev libffi-dev \
                      dpkg-dev fakeroot libfakeroot:amd64 \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install IPyLeaflet. The notebook library dependency is downgraded to
# version 4.4.1 but the datalab repo warns about potential version issues:
# https://github.com/googledatalab/datalab/blob/master/containers/base/Dockerfile#L139
#RUN pip install ipyleaflet \
#  && jupyter nbextension enable --py --sys-prefix ipyleaflet \
#  && pip install notebook

# Install the Earth Engine Python API.
RUN source activate $PYTHON_3_ENV && \
    pip uninstall -y google-api-core google-auth-httplib2 google-cloud-monitoring && \
    conda update -n base -c defaults conda && \
    conda install -y -c conda-forge google-auth-httplib2 google-cloud-storage google-cloud-monitoring && \
    pip install earthengine-api && \
    source deactivate && \
    source activate $PYTHON_2_ENV && \
    pip install earthengine-api

# Install custom files in the container's /datalab directory.
RUN cp /datalab/run.sh /datalab/base-run.sh
ADD run.sh /datalab/
RUN chmod a+x /datalab/run.sh

# Add license information for the new libraries added.
ADD datalab-ee.txt /datalab/
RUN cat /datalab/datalab-ee.txt >> /datalab/web/static/datalab.txt \
  && rm /datalab/datalab-ee.txt
ADD license-ee.txt /datalab/
RUN cat /datalab/license-ee.txt >> /datalab/license.txt \
  && rm /datalab/license-ee.txt



