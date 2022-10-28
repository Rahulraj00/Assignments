#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main (void)
{

 bool A=0,B=0,C=0,X=0;
 DDRB =  0b00100000;  //  13 pin as output 
 DDRD =  0b11100011;
 PORTD = 0b00011100;   // 2,3,4 as inputs
 

while(1)
{  

A= (PIND & (1 << PIND2)) == (1 << PIND2);
B= (PIND & (1 << PIND3)) == (1 << PIND3);
C=(PIND & (1 << PIND4)) == (1 << PIND4);
X=(!A&&!B)||(A&&C);
PORTB |= (X << 5);
}
return 0;
}
