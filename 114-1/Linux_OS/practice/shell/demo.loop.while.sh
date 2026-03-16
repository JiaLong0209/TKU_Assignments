#!/bin/bash
# demonstrate to use the while loop

condition=0;

while [ $condition -lt "5" ]
do
	echo $condition
	condition=$((condition+1))
done

exit 0
