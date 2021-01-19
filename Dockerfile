FROM pypy:3.6-slim-stretch

RUN apt update 
RUN apt -y upgrade 
RUN apt install -y build-essential
RUN apt install -y ffmpeg

# ugrade pip 
RUN pip install --upgrade pip
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# create user 
ARG user=genesis
ARG group=genesis
ARG uid=1000
ARG gid=1001
RUN adduser ${user}

USER ${user}
RUN mkdir /home/${user}/src
RUN mkdir -p /home/${user}/src/app/contentfiles
RUN mkdir /home/${user}/log

# cp project files 
ADD app/ /home/${user}/src/app/
ADD config.py /home/${user}/src/

ADD genesis-gunicorn.sh /home/${user}/src/

EXPOSE 8080

CMD ["sh", "/home/genesis/src/genesis-gunicorn.sh"]