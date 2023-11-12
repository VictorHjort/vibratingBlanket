#define vibration_pin_left 0
#define vibration_pin_right 1
#define vibration_pin_front 3
#define vibration_pin_back 4


void setup() {
  // put your setup code here, to run once:
  Serial.beggin(9600);
  pinMode(vibration_pin_left, OUTPUT);
  pinMode(vibration_pin_right, OUTPUT);
  pinMode(vibration_pin_front, OUTPUT);
  pinMode(vibration_pin_back, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    String cmd = Serial.readString();
    if (cmd == "leftOn") {
      digitalWrite(vibration_pin_left, HIGH);
    }
    if (cmd == "rightOn") {
      digitalWrite(vibration_pin_right, HIGH);
    }
    if (cmd == "frontOn") {
      digitalWrite(vibration_pin_front, HIGH);
    }
    if (cmd == "backOn") {
      digitalWrite(vibration_pin_back, HIGH);
    }
    String cmd = Serial.readString();
    if (cmd == "leftOff") {
      digitalWrite(vibration_pin_left, LOW);
    }
    if (cmd == "rightOff") {
      digitalWrite(vibration_pin_right, LOW);
    }
    if (cmd == "frontOff") {
      digitalWrite(vibration_pin_front, LOW);
    }
    if (cmd == "backOff") {
      digitalWrite(vibration_pin_back, LOW);
    }
  }
}
