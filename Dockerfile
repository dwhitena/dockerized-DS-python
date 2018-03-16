FROM ubuntu

# install dependencies 
RUN apt-get -y update --fix-missing && \
    apt-get install -y \
        python-pip \
        python-dev \
        libev4 \
        libev-dev \
        gcc \
        libxslt-dev \
        libxml2-dev \
        libffi-dev \
        python-numpy \
        python-scipy && \
    pip install --upgrade pip && \
    pip install scikit-learn flask-restful && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add our project
ADD . /

# expose the port for the API
EXPOSE 5000

# run the API 
CMD [ "python", "/api.py" ]

