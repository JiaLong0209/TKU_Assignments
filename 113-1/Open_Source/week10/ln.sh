#!/bin/bash

echo "Hello world" >> test.txt

# soft 
ln -s test.txt test_soft_link.txt 

# hard 
ln test.txt test_hard_link.txt 

rm test.txt

ll
