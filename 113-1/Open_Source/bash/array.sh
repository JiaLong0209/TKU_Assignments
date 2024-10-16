arr=('1' '2' '3' 'yabe')

echo "${arr[0]}"           # Element #0
echo "${arr[-1]}"          # Last element
echo "${arr[@]}"           # All elements, space-separated

echo "${#arr[@]}"          # Number of elements
echo "${#arr}"             # String length of the 1st element
echo "${#arr[3]}"          # String length of the Nth element

echo "${arr[@]:1:2}"       # Range (from position 3, length 2)
echo "${!arr[@]}"          # Keys of all elements, space-separated

