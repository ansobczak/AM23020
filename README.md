# AM23020
RPi Python smbus procedure to read AM23020 temperature and humidity sensor


This is just a prove of concept, so the code is not fault tolerant and the CRC check is missing. You can find CRC verification algorithm  in AM2320 documentation. 
The SM2320 return list of bytes. You can take r[:-2] bytes for CRC verification.

The procedure utilise {smbus} module, can be installed on Rpi by <pip3 install smbus>.

