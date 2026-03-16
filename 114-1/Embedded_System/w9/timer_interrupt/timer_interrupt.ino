
// C++ code
// Control LED with potentiometer

const int button_pin = 2;
const int led_pin = 7;
unsigned long previous_time = 0;
unsigned long interval = 1000;
int led_state = LOW;

void setup()
{
  
  pinMode(button_pin, INPUT);
  pinMode(led_pin, OUTPUT);

  digitalWrite(led_pin, led_state);

  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0306;
  // TCNT1 = 3036;

  TCCR1B  |= (1 << CS12); 
  TIMSK1  |= (1 << TOIE1);

  interrupts();


  Serial.begin(9600);
}

ISR(TIMER1_OVF_vect){
  led_state = !led_state;
  Serial.println("overflow");
  digitalWrite(led_pin, led_state);
  TCNT1 = 3036;
  // for  500 ms

}

void loop()
{

  // unsigned long current_time = millis();
  // int button_state = digitalRead(button_pin);
  // int diff = current_time - previous_time;

  // if(diff >= interval){

  //   Serial.println("Toggle LED");
  //   previous_time = current_time;
  //   led_state = !led_state;
  //   digitalWrite(led_pin, led_state);

  // }

  // if(button_state){
  //   interval = 100;
  // }

  // Serial.println(current_time);
  // Serial.println(button_state);


}

