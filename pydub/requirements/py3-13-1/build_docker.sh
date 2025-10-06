#!/bin/bash
if [ $# -eq 1 ];
then
    docker_name=$1
else
    docker_name="debian-pydub-python3_13_1"
fi
docker build -t $docker_name .
