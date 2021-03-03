#! /bin/bash

_kill_prev_process () {
    if [ -f ./bg_pid.txt ]
    then
        printf "\nKilling prev process...\n"
        kill -9 "$(cat bg_pid.txt)"
        echo "Killed $(cat bg_pid.txt)"
        rm bg_pid.txt
    fi
}

start_pika () {
    _kill_prev_process
    printf "\nStarting...\n"
    nohup venv/bin/python main.py > pika.log 2>&1 & echo $! > bg_pid.txt
    echo "Started $!"
}

_rootcheck () {
    if [ "$(id -u)" != "0" ]
    then
        echo "Please use sudo (root access required)"
        exit
    fi
}

main () {
    _rootcheck

    printf "start?  y\nend?    n\n"
    read -n1 ACTION

    if [ "$ACTION" == "y" ]
    then
        start_pika
    else
        printf "\nEnding...\n"
        _kill_prev_process
    fi
}

main
exit
