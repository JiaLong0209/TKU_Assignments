
// C++ code
// Control LED with potentiometer

const int button_pin = 2;
const int led_pin = 13;
bool button_state = true;
int count = 0;

void setup()
{

  pinMode(led_pin, OUTPUT);
  pinMode(button_pin, INPUT);

  Serial.begin(9600);

  digitalWrite(led_pin, button_state);

  attachInterrupt(digitalPinToInterrupt(button_pin), trigger_button_isr, FALLING);
}

void loop()
{
  count ++;
  delay(1000);
  if(count == 10){
    attachInterrupt(digitalPinToInterrupt(button_pin), trigger_button_isr, RISING);
  }
  int read_button = digitalRead(button_pin);
  Serial.println(read_button);
  Serial.println(count);

}


void trigger_button_isr(void){

  button_state = !button_state;
  digitalWrite(led_pin, button_state);
  // detachInterrupt(digitalPinToInterrupt(button_pin));
}

// sudo chmod a+rw /dev/ttyACM0
