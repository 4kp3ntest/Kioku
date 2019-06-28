#!/bin/bash

# full path
a=$(find $PWD/kelevra -name 'kelevra.indicate*')

#holy F*ck! this is horrible -> TODO
IFS='\n' read -r -a array <<< "$a"
#read array -t y <<<"$x"
#IFS=$'\n' read -rd '' -a y <<<"$a"
echo $array[0]
echo $array[1]
