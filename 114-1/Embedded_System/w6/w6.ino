
// C++ code (slave)
//

// int led_pin = 13;

// void setup()
// {

//   Serial.begin(9600);
//   pinMode(led_pin, OUTPUT);
//   digitalWrite(led_pin, LOW);

// }

// void loop()
// {

//   if (Serial.available() > 0){

    
//     Serial.println(Serial.available());
//     String read_byte = Serial.readString();
//     read_byte.trim();
    
//     digitalWrite(led_pin, (read_byte == "on" ? HIGH : LOW));
    
//     Serial.println(read_byte);
//     Serial.println(Serial.available());
//   }
// }