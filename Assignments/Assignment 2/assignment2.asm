
.include "/home/user/m328Pdef.inc"
ldi r16,0b0000100
out DDRD, r16
ldi r17,0b11111000
out DDRB,r17
ldi r17,0b11111011
out PORTB,r17
ldi r18,0b0000001
ldi r19,0b0000001
ldi r20,0b0000001

AND r18,r17   ;r17=A
LSR r17
AND r19,r17   ;r18=B
LSR r17
AND r20,r17   ;r19=C
LSR r17

ldi r21, 0b0000001
eor r21,r18  ;r20=A'
ldi r22, 0b0000001
eor r22,r19  ;r21=B'

mov r0,r21   ;r0=A'
mov r1,r22   ;r1=B'
AND r1,r0    ;r1=A'.B'

mov r2,r18   ;r2=A
mov r3,r20   ;r3=C
AND r2,r3   ;r2=A.C

OR r1,r2     ;r1=A'.B'+A.C
mov r16,r1

lsl r16
lsl r16

out portD, r16
start:
rjmp start
