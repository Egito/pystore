FROM python:3.8-buster

ENV USER=salvador
ENV UID=1000
ENV GID=1000
# default password for user
ENV PW=docker
#RUN echo ${USER} ${GID} ${UID} ${PW}
# Option1: Using unencrypted password/ specifying password
RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | \
      chpasswd
# Option2: Using the same encrypted password as host
#COPY /etc/group /etc/group 
#COPY /etc/passwd /etc/passwd
#COPY /etc/shadow /etc/shadow
# Setup default user, when enter docker container
USER ${UID}:${GID}
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /usr/bin

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
