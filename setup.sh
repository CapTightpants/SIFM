#!/bin/bash

while [ 1 == 1 ]; do
    printf '\nThis script will setup a virtual environment for SIFM and clone the configs to your printer_data. Continue? '
    read -r -n 1 -p "Y/n: " answer

    if [ -z "$answer" ]; then
        answer="y"
    fi

    case "$answer" in
        [Yy])
            break
            ;;
        [Nn])
            printf '\nGoodbye.\n'
            exit 0
            ;;
        *)
            printf '\nInvalid response.'
            clear
            ;;
    esac
done

printf '\nSetting up venv...'
python3 -m venv $HOME/SIFM/venv

printf '\nDone!\nInstalling Dependencies...\n'
./venv/bin/pip3 install -r $HOME/SIFM/requirements.txt

printf '\nDone!\nCopying configs...\n'

if [ -d $HOME/printer_data/config/ ]; then
    cp -ir $HOME/SIFM/klipper/* $HOME/printer_data/config
    printf '\nSuccess!\n'
    exit 0
else
    printf '\nprinter_data not found! Please copy the klipper configs manually.\n'
fi
