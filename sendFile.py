#file for sending file to python

import serial
import time
s = serial.Serial("/dev/ttyS4")
#/home/themakers/Cutterfiles/Test.hpgl
j = s.write(open("/home/themakers/Cutterfiles/Test.hpgl","rb").read())
#j = s.write(open("../Test.hpgl","rb").read())
time.sleep(1)
s.setDTR(0)
