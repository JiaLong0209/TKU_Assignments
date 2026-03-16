

const int led_pin = 13;

void setup()
{
  pinMode(led_pin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(led_pin, HIGH);
}

void loop()
{
  if (Serial.available())
  {
    char data = Serial.read();
    if (data == '1')
    {
      digitalWrite(led_pin, HIGH);
    }
    else if (data == '0')
    {
      digitalWrite(led_pin, LOW);
    }
  }
}