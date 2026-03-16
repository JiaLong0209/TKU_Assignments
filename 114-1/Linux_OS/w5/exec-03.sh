#!/bin/bash
# File: exec-03.sh
# Purpose: Calculate the number of days between two user-specified dates.

# --- Function: validate date input ---
get_valid_date() {
    local prompt="$1"
    local input
    local seconds
    while true; do
        read -p "$prompt (ex: yyyy-mm-dd): " input
        seconds=$(date -d "$input" +%s 2>/dev/null)
        if [ -n "$seconds" ]; then
            echo "$input"
            return 0
        else
            echo "Invalid date format. Please try again."
        fi
    done
}

# --- Function: calculate day difference ---
calc_days_diff() {
    local start="$1"
    local end="$2"
    local s_sec=$(date -d "$start" +%s)
    local e_sec=$(date -d "$end" +%s)
    local diff=$(( e_sec - s_sec ))
    if [ $diff -lt 0 ]; then
        diff=$(( diff * -1 ))
    fi
    echo $(( diff / 86400 ))
}

# --- Main program ---
start_date=$(get_valid_date "Start data")
end_date=$(get_valid_date "End data")

days_diff=$(calc_days_diff "$start_date" "$end_date")

echo "$days_diff day(s)."

