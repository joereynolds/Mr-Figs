for test in ./test/*.sh; do
    echo "Running: $test"

    # Run our game but suppress output
    ./run.py > /dev/null 2>&1 & 

    # Focus the game window
    wmctrl -a "Mr Figs"

    # Slight pause before xdotool does its thing
    # otherwise it spits all over the console
    sleep 0.5

    # s to start the game
    xdotool key --delay 1000 s > /dev/null 2>&1

    $test

    if [ $? -eq 0 ] 
    then
        echo -e '\033[0;32m'
        echo "$test"
        echo -e '\033[0m'
    else
        echo -e '\033[0;31m'
        echo "$test"
        echo -e '\033[0m'
    fi

done
