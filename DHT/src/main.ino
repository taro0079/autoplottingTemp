#include "DHT.h"
#define DHTPIN 13
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup(){

	Serial.begin(9600);
	//Serial.println("DHT11 test!");
	dht.begin();

}

void loop(){
	delay(500);

	float h = dht.readHumidity();
	float t = dht.readTemperature();

	if (isnan(h) || isnan(t)){
	
		Serial.println("Faild to read from DHT sensor!");
		return;
	}

	//Serial.println("Humidity: ");
	//Serial.print(h);
	//Serial.println("%/t");
	//Serial.print("Temperature: ");
	Serial.println(t);
	//Serial.println(" *C" );


}
