#that bloody AM2320 I2C

# prerequirenment: pip3 install smbus

import smbus
from time import sleep

i2c=smbus.SMBus(1)        #if standard Rpi Zero or 4 I2C bus is in use: GPIO 2 (I2C Data), GPIO 3 (I2C Clock)

# To test connection of AM2302 try one of the below in Python CLI. First call return error, run it twice
# i2c.read_byte(0x5c)
# i2c.read_byte_data(0x5c,0x00)

# 
# the function is just a test and prove of concept. It miss the CRC check.
# read_AM2320 usage:
# read_AM2320(i2c,0); sleep(0.1); read_AM2320(i2c,2)
# first returns relative humidity, second temperature in Celsius
# minimum 0.1s delay is required between calls due to AM2320 nature of going dormant
# the sleep times in procedure have been tested on Raspberry Pi Zero with Python 3.9


def read_AM2320(bus, ar=0x02):
   try:
      bus.read_byte(0x5c)                                #waking up the sensor
   except:
      pass
   sleep(0.015)
   bus.write_i2c_block_data(0x5c, 0x03, [ ar, 2])       #telling AM2320 to prepare data
   sleep(0.02)
   r=bus.read_i2c_block_data(0x5c, 0x3, 0x06)           #reading data from the sensor
#   print(r,end= ' ')
   if ar==0: 
      print('relative humidity (%)  : ',end= ' ')
      print((r[2]*256+r[3])/10,end= ' ')
   elif ar==2: 
      print('temperature in Celsius : ',end= ' ')
      r = (r[2]*256+r[3])/10
      if r >= 32768:
            r = 32768 - r
      print(r,end= ' ')
   else: print('unknown register: ',end= ' ')
#   print(r,end= ' ')
   print('')
