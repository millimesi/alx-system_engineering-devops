#!/usr/bin/env bash
i=1
if [ $i -eq 0 ]; then
    echo "i is zero"
elif [ $i -lt 0 ]; then
    echo "i is negative"
else
    echo "i is positive"
fi
day="monday"
case $day in
    "monday")
        echo "work day"
        ;;
    "thursday")
        echo "prayer day"
        ;;
    *)
        echo "other day"
        ;;
esac

