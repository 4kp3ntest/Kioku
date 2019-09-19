FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:freecad-maintainers/freecad-stable && \
    apt update && \
    apt-get install -y freecad git python-numpy python-pyside 

RUN mkdir ~/.FreeCAD/Mod && \
    cd ~/.FreeCAD/Mod && \
    git clone https://github.com/hamish2014/FreeCAD_assembly2.git
