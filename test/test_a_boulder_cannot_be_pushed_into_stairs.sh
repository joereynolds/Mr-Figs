xdotool key --delay 200 n
xdotool key --delay 200 n
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 q

read -p "Did boulder stop at the stairs?" answer

if [ $answer = 'y' ]; then
    exit 0
fi

exit 1
