#include <SPI.h>

const int slave_pin = 10;
// master
byte recept_data = 0;


void setup() {
  pinMode(MOSI, OUTPUT);
  pinMode(MISO, INPUT);
  pinMode(SCK, OUTPUT);
  pinMode(slave_pin, OUTPUT);

  digitalWrite(slave_pin, HIGH);

  Serial.begin(9600);
  SPI.begin();

  SPI.setclockDivider(SPI_CLOCK_DIV16); // 16MHz / 16 = 1MHz
}

void loop() {
  char send_data = 'A';

  digitalWrite(slave_pin, LOW); // select slave
  recept_data = SPI.transfer(send_data);
  Serial.println(recept_data)

  digitalWrite(slave_pin, HIGH); // select slave
  delay(1000);

}
