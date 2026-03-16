const int sensorPin = A0;
unsigned long previousTime = 0;
const unsigned long interval = 1000;

void setup()
{   
    pinMode(sensorPin, INPUT);
    
    Serial.begin(9600);
}

void loop()
{
    unsigned long currentTime = millis();
    if (currentTime - previousTime >= interval)
    {
        previousTime = currentTime;
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
    }
}