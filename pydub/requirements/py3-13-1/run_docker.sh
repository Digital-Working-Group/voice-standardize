#!/bin/bash

if [ $# -eq 1 ];
then
    container_name=$1
else
    container_name="debian-pydub-python3_13_1-ctr"
fi

if [ $# -eq 2 ];
then
    docker_name=$1
else
    docker_name="debian-pydub-python3_13_1"
fi
dir_up=$(realpath "../../../")
docker run -v $dir_up:/scripts/ -it --rm --name $container_name $docker_name bash