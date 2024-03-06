#!/bin/bash
args=$@
echo "Files: $args"
echo "-------------------"

filename=$1
name=$(echo $filename | cut -d '.' -f 1)
extension=$(echo $filename | cut -d '.' -f 2)

g++ "${name}.${extension}" -Wall -o "${name}.out" && ./"${name}.out" && rm ./"${name}.out"
# g++ "${args}"  && ./a.out && rm ./a.out


