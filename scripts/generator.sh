#!/bin/bash
#$(seq "$1")
SCALE=$1
NAME='observer_'$2
USER=$2
WORKER_RUNNING=$(sudo docker ps | grep $NAME | wc -l | xargs)

if [ "$WORKER_RUNNING" -eq "$SCALE" ] || [ "$SCALE" -eq 0 ]; then
    echo "Nothing to do"
    exit 0
fi

if [ "$WORKER_RUNNING" -gt "$SCALE" ]; then
    echo "Stopping docker containers"
    docker stop $(sudo docker ps -a -q  -f "name=$NAME")
    docker rm $(sudo docker ps -a -q  -f "name=$NAME")
fi

WORKER_RUNNING=$(docker ps | grep $NAME | wc -l | xargs)
FROM=$(expr 1 + $WORKER_RUNNING)

for i in $(seq $FROM $SCALE)
do
  n=$(printf $NAME"_%02d" $i)
  echo "Starting $n"
  docker run --name $n  -d --rm --env-file='/opt/app/.env' --env CHANNEL=$NAME --env USER=$USER user-observer:latest 
done
