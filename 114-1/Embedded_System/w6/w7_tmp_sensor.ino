// C++ code
// Control temp sensor

const int sensor_pin = A5;

void setup()
{

  pinMode(sensor_pin, INPUT);

  Serial.begin(9600);

}

void loop()
{
  int sensor_value = analogRead(sensor_pin);
  Serial.println(sensor_value);
  int temperature = (sensor_value * 5.0 / 1023.0) * 100; 
  Serial.println(temperature);
	delay(500);
  
}

// sudo chmod a+rw /dev/ttyACM0


// sudo chmod a+rw /dev/ttyACM0
