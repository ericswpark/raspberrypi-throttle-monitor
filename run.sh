#!/usr/bin/env bash

# Check if venv directory exists
if [ ! -d "venv" ]
then
    # Directory does not exist, initialize virtualenv
    virtualenv venv
    . venv/bin/activate

    # Install dependencies
    pip3 install -r requirements.txt

    python throttle-status.py
else
    # Directory exists, run immediately
    . venv/bin/activate
    python throttle-status.py
fi
