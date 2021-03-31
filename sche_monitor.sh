#!/bin/bash
while true; do
    if
        ps -ef |grep scheduler | grep -v "grep"
    then
        echo ">>>>running it"
    else
        time=$(date "+%Y%m%d-%H%M%S")
        echo "${time}>>>>restart scheduler"  >> schedulerRestart.log
        airflow scheduler
    fi
    sleep 5
done