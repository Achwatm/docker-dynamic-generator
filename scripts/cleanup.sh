#!/bin/bash

#Define cleanup procedure
cleanup() {
    echo "Container stopped, performing cleanup..."
}

#Trap SIGTERM
trap 'cleanup' SIGTERM

#Execute a command
"${@}" &
echo "Stopping docker containers"
docker stop $(sudo docker ps -a -q  -f "name=observer_")
docker rm $(sudo docker ps -a -q  -f "name=observer_")

#Wait
wait $!