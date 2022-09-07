#include <Arduino.h>
int A=1,B=0,C=1;
int X;
void setup(){
     pinMode(X,OUTPUT);
}
void loop(){
X=(!A&&!B)||(A&&C);

digitalWrite(2, X);
}
