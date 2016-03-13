[![Build Status](https://travis-ci.org/dbieber/at-scheduler.svg?branch=master)](https://travis-ci.org/dbieber/at-scheduler)

# at-scheduler
at-scheduler is a simple command line scheduler

You tell it what you want done and when you want it done, and at-scheduler gets it done.

    at 10pm say Good evening George!
    
    at 10am open https://www.google.com/search?q=youtube%20good%20morning&btnI  # that's I'm feeling lucky

## Installation

    python setup.py install

## Usage

    at <time> <command>

## Before usage

    sudo redis-server &
    sudo mkdir -p /opt/at-scheduler
    sudo python at/atd.py

This will run redis-server and the at-daemon (atd) in the background.

## Contributing
0. Leave a comment in Issues about your ideas, your plans, your grand vision!
1. Fork it!
2. Create your feature branch: `git checkout -b u/username/YYYY-MM-DD/feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
