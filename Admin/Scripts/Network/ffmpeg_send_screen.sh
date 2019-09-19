ffmpeg -r 15 -f x11grab -s 1920x1080 -i :0.0 -c:v mpeg4 -b:v 5000k -f mpegts udp://Nier.local:8888

#on Nier use
#omxplayer --live udp://0.0.0.0:8888
