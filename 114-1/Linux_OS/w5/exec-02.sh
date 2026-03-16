#!/bin/bash
# 檔名：exec-02.sh
# 功能：使用 select 建立選單，顯示不同格式的日期

echo "Please select a format of date:"

select format in \
    "Canada #dd/mm/yy" \
    "Denmark #yyyy-mm-dd" \
    "Finland #dd.mm.yyyy" \
    "French #dd/mm/yyyy" \
    "Germany #yyyy-mm-dd" \
    "Italy #dd/mm/yy" \
    "United States #mm-dd-yy"
do
    case $REPLY in
        1) date +"%d/%m/%y" ;;
        2) date +"%Y-%m-%d" ;;
        3) date +"%d.%m.%Y" ;;
        4) date +"%d/%m/%Y" ;;
        5) date +"%Y-%m-%d" ;;
        6) date +"%d/%m/%y" ;;
        7) date +"%m-%d-%y" ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
    break
done
