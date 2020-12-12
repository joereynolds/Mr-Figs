xdotool key --delay 200 n
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 q

read -p "Did the boulder get pushed?" answer

if [ $answer = 'y' ]; then
    exit 0
fi

exit 1
