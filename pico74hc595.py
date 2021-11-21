from machine import Pin
import utime
import random

#define PINs according to cabling
dataPIN = 13
latchPIN = 15
clockPIN = 14

#set pins to output PIN objects
dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)

#define shift register update function
def shift_update(data_bits,data,clock,latch):
  #put latch down to start data sending
  clock.value(0)
  latch.value(0)
  #clock.value(1)
  
  #load data in reverse order
  for i in range(7, -1, -1):
    clock.value(0)
    data.value(data_bits &(1<<i))
    clock.value(1)

#put latch up to store data on register
  clock.value(0)
  latch.value(1)
  clock.value(1)

#main program, calling shift register function


while True:
    bit_pattern = random.randint(0, 255)
    shift_update(bit_pattern,dataPIN,clockPIN,latchPIN)
    utime.sleep(0.3)
