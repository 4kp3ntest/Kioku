#!/bin/bash

jupyter notebook --no-browser &
sleep 1
firefox http://localhost:8888/
