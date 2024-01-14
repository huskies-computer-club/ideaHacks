#include <Wire.h>
#include "Adafruit_Si7021.h"

Adafruit_Si7021 sensor = Adafruit_Si7021();

struct SensorData {
  float temp;
  float humidity;
  unsigned long timestamp;
  };
  
void setup() {
  Serial.begin(9600);

  if (!sensor.begin()) {
    Serial.println("Did not find Si7021 sensor!");
    while (true);
  }
}

void loop() {
  SensorData data;
  data.temp = sensor.readTemperature();
  data.humidity = sensor.readHumidity();
  data.timestamp = millis();
  String logEntry = "timestamp:" + String(data.timestamp) + "," + "temp:" + String(data.temp) + "," + "humidity:" + String(data.humidity);
  Serial.println(logEntry);
  delay(1000);
}
