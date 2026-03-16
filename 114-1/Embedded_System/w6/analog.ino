// C++ code
//
// int analog_pin = 3;

// int brightness = 255;

// int fade_amount = -5;

// void setup()
// {
//   Serial.begin(9600);
//   pinMode(analog_pin, OUTPUT);
//   digitalWrite(analog_pin, HIGH);
// }

// void loop()
// {

//   if (brightness <= 0 || brightness >= 256){
//     fade_amount = -fade_amount;
//   }
//   brightness = brightness + fade_amount;

//   Serial.println(brightness);

//   analogWrite(analog_pin,  brightness);
  
//   delay(20);
// }