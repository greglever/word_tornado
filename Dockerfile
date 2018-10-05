FROM ubuntu:latest

RUN mkdir /word-tornado
WORKDIR /word-tornado

RUN apt-get update && \
    apt-get install -y build-essential python \
    python-dev python-pip python-virtualenv postgresql \
    postgresql-contrib libpq-dev \
    libsasl2-dev libldap2-dev libssl-dev git \
    libz-dev libffi-dev

ADD . /word-tornado

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install .

EXPOSE 8888

CMD ["python", "/word-tornado/app.py"]