FROM python

ENV USER=app
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
#USER ${UID}:${GID}
USER app
#WORKDIR /code
# create the appropriate directories
ENV HOME=/home/app
ENV PATH=${PATH}:/home/app/.local/bin
WORKDIR ${HOME}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /usr/bin

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY manage.py /home/app/
#RUN pwd && ls -lia
