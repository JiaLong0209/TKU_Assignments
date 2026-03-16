
// C++ code
// Control LED with potentiometer

const int led_pin = 3;
const int sensor_pin = A0;

void setup()
{

  pinMode(led_pin, OUTPUT);
  pinMode(sensor_pin, INPUT);

  Serial.begin(9600);

  digitalWrite(led_pin, LOW);

}

void loop()
{

  delay(100);

  int sensor_value = analogRead(sensor_pin);

  // sensor_value = sensor_value / 4;

  Serial.println(sensor_value);
  sensor_value = map(sensor_value, 0, 1023, 0, 255);

  analogWrite(led_pin, sensor_value);


}

// sudo chmod a+rw /dev/ttyACM0
