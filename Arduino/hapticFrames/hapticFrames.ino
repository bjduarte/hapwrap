//configured for: HapWrap V3
//version 0.1
#include <FastLED.h>
#include "WiFi.h"
#include <ESPAsyncWebServer.h>
#include <ArduinoJson.h>

//pin of the onboard LED
#define LED 2

//
#define DATA_PIN 12
#define NUM_LEDS 100

#define MAX_BUFF_LEN 1000

AsyncWebServer server(80);
AsyncWebSocket ws("/ws");

//acces information for various wireless networks

//const char* ssid = "troysphone";
const char* ssid = "Cubic";
const char* password = "num1ininnovation";

//const char* ssid = "chowderphone";
//const char* password = "31415926";

bool wifi = true;
bool reciv = false;

String buff[MAX_BUFF_LEN];
int buffSize = 0;
StaticJsonDocument<1000> doc;

String incoming;
CRGB leds[NUM_LEDS];

unsigned long LstartMicro;
unsigned long currMicro;
unsigned long aniStart;
int frame;
bool started = false;
int displayTime = 0;

//on a websocket event run this
void onWsEvent(AsyncWebSocket * server, AsyncWebSocketClient * client, AwsEventType type, void * arg, uint8_t *data, size_t len){
  if(type == WS_EVT_CONNECT){
    Serial.println("Websocket client connection received");
    client->text("Hello from ESP32 Server");
 
  } else if(type == WS_EVT_DISCONNECT){
    Serial.println("Client disconnected");
 
  } if(type == WS_EVT_DATA){
    Serial.println("Got Data!");
    reciv = true;

    for(int i=0; i < len; i++)
          incoming += (char) data[i];
    
    Serial.println(incoming);// incoming has the json string

    if (buffSize < MAX_BUFF_LEN)
      buff[buffSize] = incoming;//add it to the buffer of commands if there's space

    buffSize += 1;
    incoming = "";
    reciv = false;
    Serial.println("Added to Buffer!");
  }
}

void setup() {
  pinMode(LED,OUTPUT);

  //initialize strip
  FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
  for (int i = 0; i < NUM_LEDS; i++)
      leds[i] = CRGB::Black;
  FastLED.show();
  
  //initialize serial
  Serial.begin(115200);
  Serial.println("HIII");
  
  //initialize wifi
  WiFi.begin(ssid, password);

  for (int i = 0; i < 1000 && WiFi.status() != WL_CONNECTED; i++) { //try connceting to wifi a few times
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  digitalWrite(LED,HIGH);

  
  if (WiFi.status() != WL_CONNECTED){
    wifi=false;
    Serial.println("Couldn't connect to wifi </3");
  }

  
  if (wifi){
    Serial.println(WiFi.localIP());
    ws.onEvent(onWsEvent);
    server.addHandler(&ws);
    server.begin();
  }

}

void loop() {
  LstartMicro = micros();

  //parsing if data available and time to start
  if (buffSize > 0 && !started && !reciv) {
    Serial.println("got new frame!, now parsing JSON");
    Serial.println(buff[0]);
    
    int n = buff[0].length(); 
  
    char char_array[n + 1]; 
  
    strcpy(char_array, buff[0].c_str()); 
        
    DeserializationError error = deserializeJson(doc, char_array);

    // Test if parsing succeeds.
    if (error) {
      Serial.print(F("deserializeJson() failed: "));
      Serial.println(error.c_str());
      return;
    }
    
    displayTime = (int)doc["ms"];
    Serial.print("displayTime: ");
    Serial.println(displayTime);
    for (int i = 0; i <= sizeof(doc["red"]);i++) {//sizeof(doc["red"])
      Serial.print(i);
      leds[i].red =(int) doc["red"][i];
      Serial.print((int)doc["red"][i]);
      leds[i].blue =(int) doc["blue"][i];
      Serial.print((int)doc["blue"][i]);
      leds[i].green =(int) doc["green"][i];
      Serial.println((int)doc["green"][i]);
    }

    Serial.println("trying LED write");
    FastLED.show();

    //take frame off of the buffer
    for(int i = 1; i < buffSize ; i++)
      buff[i-1] = buff[i];
    buff[buffSize] = "";
    buffSize -= 1;
    started = true;
    aniStart = LstartMicro;
    Serial.println(started);
  }

//  Serial.println(started);
//  Serial.print(LstartMicro - aniStart);
//  Serial.print("\t");
//  Serial.println(displayTime * 1000);
//  
  if (LstartMicro - aniStart > displayTime * 1000 && started){
    Serial.println("Ending frame");
    for (int i = 0; i < NUM_LEDS; i++)
      leds[i] = CRGB::Black;
    FastLED.show();
    started = false;
  }

  currMicro = micros();
  if (currMicro - LstartMicro >= 0) //protect from overflows
    delayMicroseconds(50 * 1000 - (currMicro - LstartMicro));
}
