#!/bin/bash

docker build -t user-observer .

#Define cleanup procedure
cleanup() {
    echo "Container stopped, performing cleanup..."
    docker stop $(sudo docker ps -a -q  -f "name=observer_")
}

#Trap SIGTERM
trap 'cleanup' SIGTERM

#Execute a command
"${@}" &



#Wait
wait $!
cleanup