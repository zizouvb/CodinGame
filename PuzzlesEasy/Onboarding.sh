while true; do
    # enemy1: name of enemy 1
    read enemy1
    # dist1: distance to enemy 1
    read dist1
    # enemy2: name of enemy 2
    read enemy2
    # dist2: distance to enemy 2
    read dist2

    # Write an action using echo
    # To debug: echo "Debug messages..." >&2

    if [ $dist1 -gt $dist2 ]
    then
        echo $enemy2
    else
        echo $enemy1
    fi
done
