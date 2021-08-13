/*
   File  : DFRobot_SIM7000_HTTP.ino
   Power : SIM7000 needs 7-12V DC power supply
   Brief : This example verify HTTP connection over a HTTP request
           With initialization completed, we connect to server POST data and GET data
           Thus we finished the HTTP POST and GET verification
   Note  : If you use NB-IOT please confirm that the IOT is in the whitelist of your NB card
           If you use Mega please connect PIN8 PIN10 and set PIN_RX = 10
*/

#include <Wire.h>
#include <DFRobot_SIM7000.h>
#include "DFRobot_BME280.h"
#include "LowPower.h"
#include <ArduinoJson.h>


#define PIN_TX     7
#define PIN_RX     10

#define ID_Arduino  "10000010"

//This URL is use for post data to tlink (s'ha de canvair, depèn del túnel)
#define POSTURL "7b6d7bf6ca6f.ngrok.io/api/dades/update/"

// Vbles control parades
int i = 0;
int valor_max = 144; // Cada 30 min. 144    Cada 2 min. 9
int stops = 0;

SoftwareSerial     mySerial(PIN_RX, PIN_TX);
DFRobot_SIM7000    sim7000;

typedef DFRobot_BME280_IIC    BME;
BME   bme(&Wire, 0x76);
#define SEA_LEVEL_PRESSURE    1015.0f

void (*resetFunc)(void) = 0;

// PINs de connexió Arduino MEGA
const byte wind = 41;
const byte water = 2;
int vane =  A13;

// Vbles pluviometre  G i R (Un al negatiu)
const float waterIncrease = 0.2794;
float waterQuantity = 0;

// Vbles anemòmetre   N i G
unsigned long t;
float tIncrease = 5000;
float cont = 0;
float contAnt = 0;
float sample = 0;
float rFactor = 2.4;
float wSpeed = 0;
// N a positiu, G pota positiva resistencia
// connexió amb sèrie, cable a arduino per allà

// Vbles penell     V i R
float volt = 235;
String wDirection = "N";
// V a positiu, R pota positiva resistencia
// connexió amb sèrie, cable a arduino per allà


void SIM() {
  bme.reset();
  Serial.println("bme read data test");
  while (bme.begin() != BME::eStatusOK) {
    Serial.println("bme begin faild");
    printLastOperateStatus(bme.lastOperateStatus);
    delay(2000);
  }
  Serial.println("bme begin success");
  delay(100);

  float   temp = bme.getTemperature();
  uint32_t    press = bme.getPressure();
  float   humi = bme.getHumidity();

  Serial.println();
  Serial.println("======== start print ========");
  Serial.print("temperature (unit Celsius): "); Serial.println(temp);
  Serial.print("pressure (unit pa):         "); Serial.println(press);
  Serial.print("humidity (unit percent):    "); Serial.println(humi);
  Serial.println("========  end print  ========");

  delay(1000);

  int signalStrength, dataNum;
  sim7000.begin(mySerial);
  Serial.println("Turn ON SIM7000......");
  if (sim7000.turnON()) {                                  //Turn ON SIM7000
    Serial.println("Turn ON !");
  }

  Serial.println("Set baud rate......");
  while (1) {
    if (sim7000.setBaudRate(19200)) {                    //Set SIM7000 baud rate from 115200 to 19200 reduce the baud rate to avoid distortion
      Serial.println("Set baud rate:19200");
      break;
    } else {
      Serial.println("Faile to set baud rate");
      delay(1000);
      resetFunc();
    }
  }

  Serial.println("Check SIM card......");
  if (sim7000.checkSIMStatus()) {                          //Check SIM card
    Serial.println("SIM card READY");
  } else {
    Serial.println("SIM card ERROR, Check if you have insert SIM card and restart SIM7000");
    resetFunc();
  }

  Serial.println("Set net mode......");
  while (1) {
    if (sim7000.setNetMode(GPRS)) {                      //Set net mod GPRS
      Serial.println("Set GPRS mode");
      break;
    } else {
      Serial.println("Fail to set mode");
      delay(1000);
      resetFunc();
    }
  }

  Serial.println("Get signal quality......");
  signalStrength = sim7000.checkSignalQuality();           //Check signal quality from (0-30)
  Serial.print("signalStrength =");
  Serial.println(signalStrength);
  delay(500);

  Serial.println("Attaching service......");
  while (1) {
    if (sim7000.attacthService()) {                      //Open the connection
      Serial.println("Attach service");
      break;
    } else {
      Serial.println("Fail to Attach service");
      delay(1000);
      resetFunc();
    }
  }

  Serial.println("Init http......");
  while (1) {
    if (sim7000.httpInit(GPRS)) {                        //Init http service
      Serial.println("HTTP init !");
      break;
    } else {
      Serial.println("Fail to init http");
      resetFunc();
    }
  }

  windSpeed();
  windDirection();

  Serial.print("POST to ");
  //Serial.println(POSTURL);
  String httpbuff;
  // Creació del document JSON amb la llibreria ArduinoJson
  DynamicJsonDocument doc(1024);
  doc["id_station"] = ID_Arduino;
  doc["temperature"] = String(temp);
  doc["press"] = String(press);
  doc["rain"] = String(waterQuantity);
  doc["air_humidity"] = String(humi);
  doc["wind_speed"] = String(wSpeed);
  doc["wind_direction"] = wDirection;

  serializeJsonPretty(doc, httpbuff);   // Obtenció del JSON en l'string output
  Serial.print(httpbuff);

  while (1) {
    if (sim7000.httpPost(POSTURL, httpbuff)) {           //HTTP POST
      Serial.println("Post successed");
      break;
    } else {
      Serial.println("Fail to post");
    }
  }

  Serial.println("Disconnect");
  sim7000.httpDisconnect();                                //Disconnect
  Serial.println("Close net work");
  sim7000.closeNetwork();                                  //Close net work
  Serial.println("Turn off SIM7000");
  sim7000.turnOFF();                                       //Turn OFF SIM7000
}

void printLastOperateStatus(BME::eStatus_t eStatus)
{
  switch (eStatus) {
    case BME::eStatusOK:    Serial.println("everything ok"); break;
    case BME::eStatusErr:   Serial.println("unknow error"); break;
    case BME::eStatusErrDeviceNotDetected:    Serial.println("device not detected"); break;
    case BME::eStatusErrParameter:    Serial.println("parameter error"); break;
    default: Serial.println("unknow status"); break;
  }
}

void windSpeed() {
  sample = 0;
  t = millis();
  while (millis() <= t + tIncrease) {
    cont = digitalRead(wind);
    if (cont == LOW && contAnt == HIGH) {
      sample = sample + 1;
    }
    contAnt = cont;
  }
  wSpeed = sample * 1000 * rFactor / tIncrease;
}

void windDirection() { // en Nord el senyala el pluviomentre
  volt = analogRead(vane);
  if (volt > 230 && volt < 245) {
    wDirection = "N";
  }
  else if (volt > 725 && volt < 745) {
    wDirection = "S";
  }
  else if (volt > 920 && volt < 940) {
    wDirection = "E";
  }
  else if (volt > 65 && volt < 85) {
    wDirection = "W";
  }
  else if (volt > 500 && volt < 560) {
    wDirection = "NE";
  }
  else if (volt > 120 && volt < 145) {
    wDirection = "NW";
  }
  else if (volt > 790 && volt < 850) {
    wDirection = "SE";
  }
  else if (volt > 360 && volt < 400) {
    wDirection = "SW";
  }
}


void rain() {
  detachInterrupt(digitalPinToInterrupt(water));
  waterQuantity = waterQuantity + waterIncrease;
  attachInterrupt(digitalPinToInterrupt(water), rain, LOW);
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  pinMode(wind, INPUT);
  pinMode(water, INPUT_PULLUP);
  pinMode(vane, INPUT);

  attachInterrupt(digitalPinToInterrupt(water), rain, LOW);
  SIM();
}

void loop() {
  LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
  if (i > valor_max) {
    SIM();
    i = 0;
    waterQuantity = 0;
  }
  else {
    i++;
  }
}
