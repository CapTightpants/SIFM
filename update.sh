while [ 1 == 1 ]; do
    printf '\nUpdate SIFM Config files? SIFM_Settings should be manually updated. '
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

cp ~/SIFM/klipper/SIFM/* ~/printer_data/config/SIFM