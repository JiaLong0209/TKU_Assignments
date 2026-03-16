#!/bin/bash
# File: exec-04.sh
# Purpose: Check if a user-entered string is a valid IPv4 address.

read -p "Please enter an IPv4 address: " ip

# Regex for IPv4 range 0.0.0.0 ~ 255.255.255.255
regex='^([0-9]{1,3}\.){3}[0-9]{1,3}$'

if [[ $ip =~ $regex ]]; then
    # Split and check each octet’s numeric range
    IFS='.' read -r o1 o2 o3 o4 <<< "$ip"
    octets=($o1 $o2 $o3 $o4)
    for n in "${octets[@]}"; do
        # ensure numeric and in 0..255
        if ! [[ $n =~ ^[0-9]+$ ]] || (( n < 0 || n > 255 )); then
            echo "$ip is NOT a valid IPv4 address."
            exit 1
        fi
    done
    echo "$ip is a valid IPv4 address."
    exit 0
fi

echo "$ip is NOT a valid IPv4 address."
exit 1