package: docker
===============

## test installation
docker run hello-world

## debug
docker stats

## find image
docker search <substring>
docker pull <image>

## create new network with custom address space and gateway
docker network create --subnet=192.168.1.0/24 --gateway=192.168.1.2 name
docker network inspect ...

## Network bridge is the default with access to all local networks
docker network create --subnet=192.168.1.0/24 -o "com.docker.network.bridge.name"="target1" target1
docker network connect rednet red1

## docker build
docker build -f some_dockerfile -t name:optional_tag .

## RUN
(every RUN statement creates NEW LAYER!)
docker run -it --privileged --net rednet --name red1 --hostname red kali bash
docker run -dt --privileged --net rednet --name red2 --hostname red --ip 192.168.1.120 kali bash
docker build -t name /Path/to/Dockerfile
docker exec -it red1 bash

## mount local X11 socket 
sudo docker run -it --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
-v /home/gnome/Real\[salia\]/9xAndroid/android-studio-ide-173.4819257-linux/android-studio:/opt/android-studio \
android:thyrlian /opt/android-studio/bin/studio.sh

# docker-compose
## DO NOT HAVE LINES CONTAINING TABS IN FILE
docker-compose up/down #automatically creates dedicated bridge interface and removes it afterwards
docker-compose ps
docker-compose logs
docker-compose top

# Plug & Play Repos
## DVWA
https://github.com/ethicalhack3r/DVWA.git
docker run --rm -it -p 8000:80 vulnerables/web-dvwa
## Apache
httpd 
docker run -dit -p 8000:80 -v $PWD/Skills/Docker.md:/usr/local/apache2/htdocs/index.html httpd
/usr/local/apache2/htdocs/index.html
