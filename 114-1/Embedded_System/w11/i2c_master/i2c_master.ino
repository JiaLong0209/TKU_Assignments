#include <Wire.h>
void setup()
{
    Wire.begin(); // Initialize I2C as Master
}
void loop()
{
    Wire.beginTransmission(8); // Address of the Slave
    Wire.write("Hello Slave"); // Send message to the Slave
    Wire.endTransmission();    // End transmission
    delay(1000);               // Wait 1 second before sending again
}
