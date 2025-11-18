#include <WiFi.h>
#include "Adafruit_SHT31.h"
#include <Wire.h>
#define SSID "RCMP Surveillance Network-9"
#define PASS "nxmu7585"
WiFiUDP udp;
Adafruit_SHT31 sht1 = Adafruit_SHT31(); // on init sans adresse -> on peut préciser
Adafruit_SHT31 sht2 = Adafruit_SHT31();
int PORT = 12345;
char myPacket[255];
int dataLen;
String ping;
String response;
String pingMsg = "\nWaiting for ping";
float temp1, temp2;
int clientPort;
IPAddress clientIP;
/*bool packetParsed = false;*/
void setup() {
  Serial.begin(9600);
  Wire.begin(21, 22); // SDA = 21, SCL = 22 (optionnel, Wire.begin() sans args souvent OK)
  sht1.begin(0x44);
  sht2.begin(0x45);

  Serial.print("Connecting to ");
  Serial.println(SSID);
  WiFi.begin(SSID, PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());
  udp.begin(PORT);
  Serial.print("\nUDP Server started on port ");
  Serial.print(PORT);

  
  // put your setup code here, to run once:
}
 
void loop() {
  // put your main code here, to run repeatedly:
  float t1 = sht1.readTemperature();
  float h1 = sht1.readHumidity();
  float t2 = sht2.readTemperature();
  float h2 = sht2.readHumidity();

  Serial.println(pingMsg);
  if (udp.parsePacket())
  {  
    pingMsg = "";
    dataLen = udp.available();
    clientIP = udp.remoteIP();
    clientPort = udp.remotePort();
    udp.read(myPacket,255);
    myPacket[dataLen]=0;
    ping = String(myPacket);
    ping.trim();
    Serial.println("Received ping: "+ping);
  }

  if (ping == "ping"){
    response = String(t1,2) +","+ String(t2,2)+","+ String(h1,2)+","+ String(h2,2);  
    udp.beginPacket(clientIP, clientPort);
    udp.print(response);
    udp.endPacket();
    Serial.println("SENT: "+response);
    delay(1000);
  
  }
  delay(2000);
}