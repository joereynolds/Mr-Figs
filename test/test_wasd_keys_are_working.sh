xdotool key --delay 200 d
xdotool key --delay 200 d
xdotool key --delay 200 s
xdotool key --delay 200 d
xdotool key --delay 200 a
xdotool key --delay 200 w
xdotool key --delay 200 q

read -p "Are the WASD keys working? (did the player move around)" answer

if [ $answer = 'y' ]; then
    exit 0
fi

exit 1
