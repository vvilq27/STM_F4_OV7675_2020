import time
import serial
from serial import Serial
import os
from time import sleep


# while True:

# file = open("data.txt", "wb")
s = serial.Serial('COM7', 115200, timeout=0.2)

# ser.readline()
# for count in range(10):

t = list()

for i in range(0,10):
	print("round: {}".format(i))
	# s.write("dupa1".encode("UTF-8"))
	s.write("1".encode("UTF-8"))
	# sleep(0.01)
	# s.write(b'u')
	# sleep(0.01)
	# s.write(b'p')
	# sleep(0.01)
	# s.write(b'a')
	# sleep(0.01)
	# s.write(b'1')
	# sleep(0.01)
	# s.write(b'2')
	# sleep(0.01)

	# l = s.readlines()
	l = s.read(1)
	print(l)
	# sleep(0.1)




'''
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

'''