'''
Package Setup:
 - Uninstall serial using pip3 uninstall serial first
 - Install pyserial using pip3 install pyserial
TX2 Setup:
 - If using GPIO
 - If code raises SerialException: device reports readiness to read but returned no data
 	- Disable serial login prompt:
 		- edit /lib/systemd/system/serial-getty@.service
 		- change 'ExecStart...' to ExecStart=-/sbin/agetty --autologin mendel --keep-baud 115200,38400,9600 %I $TERM
'''
from serial import Serial

import time

#port=Serial("/dev/ttyUSB0",baudrate=115200,timeout=3.0) #usb
port=Serial("/dev/ttyS0",baudrate=115200,timeout=3.0)	#gpio

while True:
	try:
		time.sleep(0.01)
		print(port.readline())
	except Exception as e:
		print(e)
		#port.close()
		
port.close()
