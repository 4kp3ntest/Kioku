package: docker
===============

# debug
docker stats

# find image
docker search <substring>
docker pull <image>

# create new network with custom address space and gateway
docker network create --subnet=192.168.1.0/24 --gateway=192.168.1.2 name

# Network bridge is the default with access to all local networks
docker network create --subnet=192.168.1.0/24 -o "com.docker.network.bridge.name"="target1" target1
docker network connect rednet red1

# RUN
docker run -it --privileged --net rednet --name red1 --hostname red kali bash
docker run -dt --privileged --net rednet --name red2 --hostname red --ip 192.168.1.120 kali bash
docker build -t name /Path/to/Dockerfile
docker exec -it red1 bash

# mount local X11 socket 
sudo docker run -it --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
-v /home/gnome/Real\[salia\]/9xAndroid/android-studio-ide-173.4819257-linux/android-studio:/opt/android-studio \
android:thyrlian /opt/android-studio/bin/studio.sh


