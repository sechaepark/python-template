#!/bin/bash

SCRIPT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
APP_PATH="$(dirname $SCRIPT_PATH)"
LOG_PATH="$APP_PATH/logs"

PID_FILE="$SCRIPT_PATH/daemon.pid"
LOG_FILE="$APP_PATH/logs/daemon.$(date '+%Y%m%d').log"

mkdir -p $LOG_PATH

help_msg() {
  echo "usage: $0 [start|stop|restart]"
  echo "ex: $0 start"
  exit 1
}

if [ -f $PID_FILE ]; then
  PID=$(cat $PID_FILE)
fi

start_server() {
  if [ -f $PID_FILE ]; then
    echo "Already Started pid[$PID]"
    echo "$(date) : already exist process pid[$PID]" >>$LOG_FILE
  else
    cd $APP_PATH/app
    pipenv run python3 main.py >/dev/null 2>&1 &
    PID=$(echo $!)
    echo "$PID" >$PID_FILE
    echo "Started pid[$PID]"
    echo "$(date) : started proccess pid[$PID]" >>$LOG_FILE
  fi
}

stop_server() {
  if [ -f $PID_FILE ]; then
    kill -9 $PID
    rm $PID_FILE
    echo "Stopped pid[$PID]"
    echo "$(date) : stopped proccess pid[$PID]" >>$LOG_FILE
  else
    echo "Not found PID File[$PID_FILE]"
    echo "$(date) : not found pid file[$PID_FILE]" >>$LOG_FILE
  fi
}

reload_server() {
  if [ -f $PID_FILE ]; then
    stop_server
    start_server
  else
    start_server
  fi
}

case "$1" in
start)
  start_server
  ;;
stop)
  stop_server
  ;;
restart)
  stop_server
  sleep 3
  start_server
  ;;
*)
  help_msg
  ;;
esac

exit 0
