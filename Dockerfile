FROM python:3

RUN mkdir /word-tornado
WORKDIR /word-tornado
ADD . /word-tornado

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install .

EXPOSE 8888

CMD ["python", "/word-tornado/app.py"]
