#include <Keyboard.h>
#include <FastLED.h>
#define DATA_PIN 2
#define NUM_LEDS 68
CRGB leds[NUM_LEDS];

int standardA, standardB, standardC, standardD;
int SensorA, SensorB, SensorC, SensorD;
unsigned long tA;
unsigned long tB;
unsigned long tC;
unsigned long tD;

int delaytime = 100; //觸發延遲

//敲擊力道
int sensorvarA = 400; 
int sensorvarB = 400;
int sensorvarC = 400;
int sensorvarD = 400;

int ColorA, ColorB, ColorC, ColorD;

void setup() { // put your setup code here, to run once:
  Keyboard.begin(); // initialize control over the keyboard
  Keyboard.releaseAll();

  FastLED.addLeds<WS2812, DATA_PIN, RGB>(leds, NUM_LEDS);
  delay(1000);
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  standardA = analogRead( A0 );
  standardB = analogRead( A1 );
  standardC = analogRead( A7 );
  standardD = analogRead( A6 );
  Serial.print(" START   ");
  Serial.print(standardA);
  Serial.print("  ");
  Serial.print(standardB);
  Serial.print("  ");
  Serial.print(standardC);
  Serial.print("  ");
  Serial.print(standardD);
  Serial.println();

}

void loop() { // put your main code here, to run repeatedly:

  SensorA = analogRead(A0);
  SensorB = analogRead(A1);
  SensorC = analogRead(A7);
  SensorD = analogRead(A6);

  if (standardA - SensorA > sensorvarA && SensorA < SensorB - sensorvarA / 2 &&  millis() - tA > delaytime ) {
    Keyboard.print("d");
    tA = millis();
    ColorA = 255;
  }

  if (standardB - SensorB > sensorvarB && SensorB < SensorA - sensorvarB / 2 &&  millis() - tA > delaytime ) {
    Keyboard.print("f");
    tA = millis();
    ColorB = 255;
  }

  if (standardC - SensorC > sensorvarC && SensorC < SensorD - sensorvarC / 2 &&  millis() - tC > delaytime ) {
    Keyboard.print("j");
    tC = millis();
    ColorC = 255;
  }

  if (standardD - SensorD > sensorvarD && SensorD < SensorC - sensorvarD / 2 &&   millis() - tC > delaytime ) {
    Keyboard.print("k");
    tC = millis();
    ColorD = 255;
  }

  ColorA --;
  ColorB --;
  ColorC --;
  ColorD --;
  
  if (ColorA < 0)
    ColorA = 0;
  if (ColorB < 0)
    ColorB = 0;
  if (ColorC < 0)
    ColorC = 0;
  if (ColorD < 0)
    ColorD = 0;

//LED發光
  for (int i = 0 ; i < 24; i++) {
    leds[i] = CHSV(95, 255, ColorB);
  }

  for (int i = 24 ; i < 48; i++) {
    leds[i] = CHSV(95, 255, ColorC);
  }

  for (int i = 48 ; i < 58; i++) {
    leds[i] = CHSV(170, 255, ColorD);
  }

  for (int i = 58 ; i < 68; i++) {
    leds[i] = CHSV(170, 255, ColorA);
  }
  
  FastLED.show();
}
