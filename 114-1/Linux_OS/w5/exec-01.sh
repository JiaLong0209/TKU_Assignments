#!/bin/bash

echo "How tall are you? (cm)"
read height_cm

echo "How much do you weigh?(kg)"
read weight_kg

height_m=$(echo "scale=2; $height_cm / 100" | bc)

bmi=$(echo "scale=2; $weight_kg / ($height_m * $height_m)" | bc)

echo "==========Result============"
echo "Your BMI is $bmi"
