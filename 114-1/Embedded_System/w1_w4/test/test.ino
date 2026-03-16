// C++ code



//////////////////////////////////////////////////////////////////////////
// Controlling an LED using a pushbutton
//• Initializes pin 2 as an input (for the pushbutton) and pin 13 as an output (for the LED)
//• Each time the button is pressed, the state of the LED should toggle.
//• Turn on if it’s off, and turn off if it’s on

int button_pin = 2;
int led = 13;
bool led_state = true;

void setup()
{
   
  pinMode(button_pin, INPUT);
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  Serial.begin(9600); // bit per second

}

void loop()
{
  int button_state = digitalRead(button_pin);
  // Serial.println(button_state);

  
  if(!button_state){
    led_state = true ? led_state == false : false;
    digitalWrite(led, led_state);
  }

}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Traffic Light Simulation
// • Create a traffic light simulation using three LEDs (Red, Yellow, Green) to represent the light
// • Add a pedestrian button(pull-up) to stop the traffic and turn on the Green LED for pedestrians.
// • The button triggers the red light to stay on for 5 seconds, the yellow light to stay on for 2 seconds,
// allowing pedestrians to cross safely.
// • Red(initial condition)
// • If: Press the button
// • 5 seconds: Red -> 2 seconds: Yellow
// • Change Yellow light to Green light 10s
// Registers & Peripherals in Embedded Systems
// 45


// int button_pin = 2;
// int led = 5;
// void setup()
// {
   
//   pinMode(button_pin, INPUT);
//   pinMode(led, OUTPUT);
// }

// void loop()
// { 
//   int button_state = digitalRead(button_pin);
  
//   if(button_state){
  
//     digitalWrite(led, HIGH);

//   }else {
//     digitalWrite(led, LOW);

//   }
// }

//////////////////////////////////////////////////////////////////////////////////////////////////

// const int btn_pin = 5;
// const int led_pins[3] = {2,3,4}; // Red, Yellow, Green
// const int delays[3] = {5000, 2000, 10000};
// int speed_up = 5;

// void reset(){
//   for (int i = 0; i < 3; i++){
//     pinMode(led_pins[i], OUTPUT);
//     digitalWrite(led_pins[i], HIGH);
//   }
// }

// void setup()
// {
//   reset();

// }

// void pedestrian_led(){
//     for (int i = 0; i < 3; i++){
//       digitalWrite(led_pins[i], LOW);
//       delay(delays[i] / speed_up); 
//       digitalWrite(led_pins[i], HIGH);
//     }
// }

// void loop()
// {
//   int button_state = digitalRead(btn_pin);
//   if(button_state == LOW){
//     pedestrian_led();
//   }
//   else{
//     reset();
//   }
// }