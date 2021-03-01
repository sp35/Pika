#! /bin/bash

_kill_prev_process () {
    if [ -f ./bg_pid.txt ]
    then
        printf "\nKilling prev process...\n"
        sudo kill -9 "$(cat bg_pid.txt)"
        echo "Killed $(cat bg_pid.txt)"
        rm bg_pid.txt
    fi
}

start_pika () {
    _kill_prev_process
    printf "\nStarting...\n"
    sudo nohup venv/bin/python main.py > pika.log 2>&1 &
    echo $! > bg_pid.txt
    echo "Started $!"
}

main () {
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
