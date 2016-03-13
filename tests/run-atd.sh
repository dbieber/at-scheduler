#!/bin/bash

# Start the daemon
sudo python at/atd.py
sleep 2
sudo pkill -F /var/run/at-scheduler.pid
