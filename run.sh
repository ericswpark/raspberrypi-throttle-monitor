#!/usr/bin/env bash

# Check if venv directory exists
if [ ! -d "venv" ]
then
    # Directory does not exist, initialize virtualenv
    virtualenv venv
fi

# Activate virtualenv
. venv/bin/activate

# Check for any updates to requirements
pip3 install -r requirements.txt

# Start script
python throttle-status.py
