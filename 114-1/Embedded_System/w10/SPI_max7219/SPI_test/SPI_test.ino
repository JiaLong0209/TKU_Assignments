#include <LedControl.h>
LedControl lc = LedControl(11, 13, 10, 1); // Initialize library

// Define the letter "J"
byte J[8] = {
    B00110011,
    B01100011,
    B11100011,
    B11000011,
    B11111111,
    B01111111,
    B00000011,
    B00000011
};

// Define the letter "I"
byte I[8] = {
    B11000011,
    B11000011,
    B11000011,
    B11111111,
    B11111111,
    B11000011,
    B11000011,
    B11000011
};

// Define the letter "A"
byte A[8] = {
    B11110000,
    B11111100,
    B00101111,
    B00100011,
    B00100011,
    B00101110,
    B11111100,
    B11110000
};

// Define the letter "L"
byte L[8] = {
    B11111111,
    B11111111,
    B11000000,
    B11000000,
    B11000000,
    B11000000,
    B11000000,
    B11000000
};

// Define the letter "O"
byte O[8] = {
    B01111110,
    B11111111,
    B11000011,
    B11000011,
    B11000011,
    B11000011,
    B11111111,
    B01111110
};

// Define the letter "N"
byte N[8] = {
    B11111111,
    B11111111,
    B00000011,
    B00001110,
    B00111100,
    B01110000,
    B11111111,
    B11111111
};

// Define the letter "G"
byte G[8] = {
    B01111110,
    B11111111,
    B11000011,
    B11000011,
    B11011011,
    B11011011,
    B11111011,
    B01110010
};

// Define a 2D array to store the letters
byte my_name[7][8];

void setup()
{
    // Copy the letters into the my_name array
    for (int i = 0; i < 8; i++)
    {
        my_name[0][i] = J[i];
        my_name[1][i] = I[i];
        my_name[2][i] = A[i];
        my_name[3][i] = L[i];
        my_name[4][i] = O[i];
        my_name[5][i] = N[i];
        my_name[6][i] = G[i];
    }

    lc.shutdown(0, false); // Wake up MAX7219
    lc.setIntensity(0, 8); // Set brightness
    lc.clearDisplay(0);    // Clear display
}

void loop()
{
    // Loop through the letters in the my_name array
    for (int i = 0; i < 7; i++)
    {
        displayLetter(my_name[i]);
        delay(300);
    }
}

void displayLetter(byte letter[8])
{
    for (int i = 0; i < 8; i++)
    {
        lc.setRow(0, i, letter[i]); // Set each row of the matrix
    }
}

// 