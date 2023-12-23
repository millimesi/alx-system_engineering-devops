#!/usr/bin/env bash
i=1
while [ $i -lt 5 ]; do
    echo "i=$i and less than 5"
    ((i++))
done
i=1
until [ $i -gt 5 ]; do
    echo "i=$i and is not less than 5"
    ((i++))
done
for i in {1..5}; do
    echo "iteration $i"
done