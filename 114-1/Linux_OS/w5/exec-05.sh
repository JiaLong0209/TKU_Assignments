# !/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# File: exec-05.sh
# Purpose: Generate N random even numbers in [0..200] and print the largest.
# Usage: bash exec-05.sh [N]
# Default N is 3.


generate_even() {
    printf '%d' $(( (RANDOM % 101) * 2 ))
}


main() {
    local count=${1:-3}   # default to 3 numbers if no argument
    if ! [[ "$count" =~ ^[0-9]+$ ]] || [ "$count" -le 0 ]; then
        printf 'Invalid count: %s. Must be a positive integer.\n' "$count" >&2
        exit 1
    fi

    local nums=()
    local max=-1
    local n

    for ((i=0; i<count; i++)); do
        n=$(generate_even)
        nums+=("$n")
        (( n > max )) && max=$n
    done

    # Print generated numbers joined by ", "
    printf 'Generated numbers: %s\n' "$(IFS=', '; echo "${nums[*]}")"
    printf 'The largest number is: %d\n' "$max"
}

main "${@:-}"
