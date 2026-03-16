#!/bin/bash
# demonstrate the for loop

echo "Print 1 to 10 in method one."
for i in $(seq 1 10)
do
	echo "number: $i"
done

echo "Print 1 to 10 in method two."
for i in {1..10}
do
	echo "number: $i"
done

echo "Print odd numbers from 1 to 10."
for i in {1..10..2}
do
	echo "odd number: $i"
done

exit 0
