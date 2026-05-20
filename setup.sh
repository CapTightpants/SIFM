#!/bin/bash

while [True]; do
    printf '\nThis script will setup a virtual environment for SIFM and clone the configs to your printer_data. Continue? '
    read -r -n 1 -p "Y/n: " answer

    if [ -z "$answer" ]; then
        $answer = "y"
    fi

    case "$answer" in
        [Yy])
            break
            ;;
        [Nn])
            printf 'Goodbye.'
            exit [N]
            ;;
        *)
            printf '\nInvalid response.'
            clear
            ;;
    esac

printf '\nSetting up venv...'
python3 -m venv ~/SIFM/venv

printf '\nDone!\nInstalling Dependencies...'
./venv/bin/pip3 install -r ~/SIFM/requirements.txt

printf '\nDone!\nCopying configs...'

if [ -d "~/printer_data/config/" ]; then
    cp ~/SIFM/klipper/* ~/printer_data/config
    printf '\nSuccess!'
else
    printf '\nprinter_data not found! Please copy the klipper configs manually.'
fi