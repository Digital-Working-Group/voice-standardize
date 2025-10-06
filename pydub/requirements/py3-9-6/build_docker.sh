#!/bin/bash
if [ $# -eq 1 ];
then
    docker_name=$1
else
    docker_name="debian-pydub-python3_9_6"
fi
docker build -t $docker_name .
