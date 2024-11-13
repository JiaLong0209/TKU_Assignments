#!/bin/bash

# Associative array (aka Dictionary object)
declare -A sounds

sounds[dog]="Bark"
sounds[cow]="Moo"
sounds[bird]="Tweet"
sounds[wolf]="Howl"


for key in "${!sounds[@]}"; do 
    echo $key
done


echo ""

for value in "${sounds[@]}"; do 
    echo $value
done

info () {
    echo "---- Info  -----"
    echo ${sounds[@]}
    echo ${!sounds[@]}
    echo ${#sounds[@]}
    echo "----"
}

info

unset sounds[dog]

info

for key in "${!sounds[@]}"; do 
    echo "Unset ${key}"
    unset sounds[$key]
done

info
