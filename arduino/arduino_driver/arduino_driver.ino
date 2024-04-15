#include <LiquidCrystal.h>
#include <dht_nonblocking.h>

#define DHT_TYPE DHT_TYPE_11

static const int DHT_PIN = 2;

DHT_nonblocking dht_sensor(DHT_PIN, DHT_TYPE);
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin(16,2);

}

static bool measure(float *temp, float *humid) {
  static unsigned long int measurement_timestamp = millis();

  if (millis() - measurement_timestamp > 3000ul) {
    if (dht_sensor.measure(temp,humid) == true) {
      measurement_timestamp = millis();
      return true;
    }
  }
  return false;
  
}

static void update_lcd(float temp, float humid) {
  // Print Temperature
  lcd.setCursor(0,0);
  lcd.print("Temperature: ");
  lcd.print(temp,1);
  lcd.print(" deg. C");

  // Print Humidity
  lcd.setCursor(0,1);
  lcd.print("Humidity: ");
  lcd.print(humid,1);
  lcd.print("%");
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp;
  float humid;

  if(measure( &temp, &humid)){
    update_lcd(temp,humid);
    Serial.print(temp,1);
    Serial.print("-");
    Serial.println(humid,1);
  }
}
