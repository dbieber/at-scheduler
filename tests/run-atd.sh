#!/bin/bash

sudo python setup.py install
sudo redis-server

# Start the daemon
sudo python at/atd.py

at in 1 second 'echo test > test.out'
# TODO(dbieber): assert no file at /opt/at-scheduler/test.out
cat /opt/at-scheduler/test.out
sleep 2
# TODO(dbieber): assert file at /opt/at-scheduler/test.out
cat /opt/at-scheduler/test.out

sudo rm /opt/at-scheduler/test.out
sudo pkill -F /var/run/at-scheduler.pid
