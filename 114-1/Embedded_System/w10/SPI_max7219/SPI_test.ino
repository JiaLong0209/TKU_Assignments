// install max7219  library first
// led control libray
#include <SPI.h>

const int slaveSelect = 10;
byte recievedData;
void setup()
{
  pinMode(MOSI, INPUT);
  pinMode(MISO, OUTPUT);
  pinMode(SCK, INPUT);
  pinMode(slaveSelect, INPUT);

  // SPI.setClockDivider(SPI_CLOCK_DIV16);

  SPCR |= _BV(SPE);
  SPCR &= ~_BV(MSTR);
  Serial.begin(9600);
}
void loop()
{
  if (bitRead(SPSR, SPIF) == HIGH && SPDR == 65)
  {
    recievedData = SPDR;

    Serial.println((char)recievedData);
    SPDR = 66;
  }
}