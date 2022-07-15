FROM python:2

WORKDIR /usr/src/webserver

COPY . .

EXPOSE 80

CMD ["python2","./web-server.py"]
