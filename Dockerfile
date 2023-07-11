FROM puckel/docker-airflow:1.10.9

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV MY_APP_SECRET ${MY_APP_SECRET}

COPY ./ ./

RUN pip install -r ./requirements.txt

LABEL maintainer="mehdisamsami@live.com"
