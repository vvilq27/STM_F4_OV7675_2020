import time
import serial
from serial import Serial
import os


# while True:

file = open("data.txt", "wb")
s = serial.Serial('COM7', 2000000)

# ser.readline()
# for count in range(10):

t = list()



while True:
	l = s.readline()
	if b'' in l or b'hscnt' in l:
		break
	if int(l.decode("UTF-8").rstrip('\r\n').split(',').pop()) < 10:
		break

while True:
	l = s.readline()
	if int(l.decode("UTF-8").rstrip('\r\n').split(',').pop()) > 238:
		break
	t.append(l)
	# file.write(l)



	# if b"hscnt" in l:
	# 	break
print(len(t))
for line in t:
	file.write(line)

file.close()
s.close()

# print(t[len(t)-1])

print("img")
os.system("imageMakerFile.py 1")

