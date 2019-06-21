ARG IMAGE_VERSION

FROM python:$IMAGE_VERSION

WORKDIR /usr/src/app

RUN apt update && apt install tcpdump iptables 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#ENV FLASK_APP=app.py
#CMD ipython 
