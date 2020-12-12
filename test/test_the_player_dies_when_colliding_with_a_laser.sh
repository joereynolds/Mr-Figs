xdotool key --delay 200 n
xdotool key --delay 200 n
xdotool key --delay 200 n
xdotool key --delay 200 n
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Down
xdotool key --delay 200 Down
xdotool key --delay 200 q

read -p "Did the player die?" answer

if [ $answer = 'y' ]; then
    exit 0
fi

exit 1
