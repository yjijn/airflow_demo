#!/bin/bash
while true; do
    if
        ps -ef |grep Worker | grep -v "grep"
    then
        echo ">>>>running it"
    else
        time=$(date "+%Y%m%d-%H%M%S")
        echo "${time}>>>>restart worker"  >> workerRestart.log
        airflow worker
    fi
    sleep 5
done