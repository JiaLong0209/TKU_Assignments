#!/bin/bash
# demonstrate conditional expressions if/else

declare -i random_number_a=$RANDOM%100+1
declare -i random_number_b=$RANDOM%100+1

echo "Automatically generate an integer a = $random_number_a (1~100)".
echo "Automatically gererate an integer b = $random_number_b (1~100)".

if [ $random_number_a -gt $random_number_b ]
then
	echo "a > b"
elif [ $random_number_a -lt $random_number_b ]
then
	echo "a < b"
else
	echo "a = b"
fi

exit 0


# operator
# -f: check the path is file or not.        Yes (return true); No (return false)
# -d: check the path is directory or not.   Yes (return true); No (return false)
# -r: check the file/directory is readable or not.    Yes (return true); No (return false)
# -w: check the file/directory is writable or not.    Yes (return true); No (return false)
# -x: check the file/directory is executable or not.  Yes (return true): No (return false)
# -n: check the variable is null or not.         Not null (return true); Is null (return false)
# -z: check the varuable is null or not.          Is null (return true): Not null (return false)
# -eq: It means "=="  (equal)
# -ne: It means "!="  (not equal)
# -gt: It means ">"
# -ge: It means ">=" (greater than and equal)
# -lt: It means "<"
# -le: It means "<="
