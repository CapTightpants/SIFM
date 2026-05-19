#!/bin/bash

printf 'Setting up venv...\n'
python3 -m venv ./venv

printf '\nDone!\nInstalling Dependencies...\n'
./venv/bin/pip3 install -r ./requirements.txt
