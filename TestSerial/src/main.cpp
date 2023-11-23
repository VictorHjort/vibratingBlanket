#include <Arduino.h> 

int LEFT = 2;
int RIGHT = 3;
int FRONT = 4;
int BACK = 5;
int var = 0;
int turnOff = 0;
int low = 85;
int medium = 170;
int high = 255;

void setup() { 
	Serial.begin(115200); 
	Serial.setTimeout(1); 
  pinMode(LEFT, OUTPUT);
} 
void loop() { 
	while (!Serial.available()); 
	var = Serial.readString().toInt(); 
	Serial.print(var); 

	switch (var) {
		case 1:
		analogWrite(LEFT, turnOff);
		break;

		case 2:
		analogWrite(LEFT, low);
		break;

		case 3:
		analogWrite(LEFT, medium);
		break;

		case 4:
		analogWrite(LEFT, high);
		break;

		case 5:
		analogWrite(RIGHT, turnOff);
		break;

		case 6:
		analogWrite(RIGHT, low);
		break;

		case 7:
		analogWrite(RIGHT, medium);
		break;

		case 8:
		analogWrite(RIGHT, high);
		break;

		case 9:
		analogWrite(FRONT, turnOff);
		break;

		case 10:
		analogWrite(FRONT, low);
		break;

		case 11:
		analogWrite(FRONT, medium);
		break;

		case 12:
		analogWrite(FRONT, high);
		break;

		case 13:
		analogWrite(BACK, turnOff);
		break;

		case 14:
		analogWrite(BACK, low);
		break;

		case 15:
		analogWrite(BACK, medium);
		break;

		case 16:
		analogWrite(BACK, high);
		break;
	}
	var = 0;
} 


