#!/bin/bash

# If any command fails, we consider the tests to have failed
set -e

sudo mkdir -p /opt/at-scheduler
sudo python setup.py install
sudo redis-server &

# Start the daemon
sudo python at/atd.py

# Test 1: After 1 second, write "Jelly and bread!" to test.out
at in 1 second 'echo Jelly and bread! > test.out'

# First, assert the file does not exist.
if [ -f "/opt/at-scheduler/test.out" ]
then
    exit 1
fi

sleep 2  #

# Now, assert the file does exist.
if [ ! -f "/opt/at-scheduler/test.out" ]
then
    exit 1
fi
# And furthermore assert that the file has the proper text
text=`cat /opt/at-scheduler/test.out`
if [ "$text" != 'Jelly and bread!' ]
then
    exit 1
fi

sudo rm /opt/at-scheduler/test.out
sudo pkill -F /var/run/at-scheduler.pid
