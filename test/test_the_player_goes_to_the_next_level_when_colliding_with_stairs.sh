xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Down
xdotool key --delay 200 Right
xdotool key --delay 200 Down
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Up
xdotool key --delay 200 Up
xdotool key --delay 200 Right
xdotool key --delay 200 q

read -p "Did the user get taken to the next level after going to the stairs?" answer

if [ $answer = 'y' ]; then
    exit 0
fi

exit 1
