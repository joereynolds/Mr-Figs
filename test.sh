./run.py &

echo 'Test we go to the next level when we hit the stairs'
xdotool type --delay 2000 s 
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 200 Right
xdotool key --delay 500 Right
xdotool key --delay 500 Right
xdotool key --delay 500 Right

read -p "Did the user get taken to the next level after going to the stairs?" answer

# There's a random s coming in the input from above somehow
if [ $answer = 'sy' ]; then
    echo -e '\033[0;32m Test passed!'
    echo -e '\033[0m'
fi

xdotool key --delay 500 Right
xdotool key --delay 500 Right
