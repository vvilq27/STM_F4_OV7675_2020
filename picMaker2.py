import time
import serial
from serial import Serial		#pip install pyserial (not serial)
import os

import re
import numpy as np

from matplotlib import pyplot as plt

from sorter import sort

import threading

# TODO 
# check on mcu side whats sent
#  check on python side whats received
# how its parsed and errors catched


# split it to two threds: 1. creates image 2. saves to file

rowRange = 240
pic = []
t = []
d = {}
listLinesToCapture = list(range(rowRange))

file = open('data.txt', 'w')

pic = [ ['00' for i in range(320)] for j in range(240)]
s = serial.Serial('COM8', 1000000, timeout=0.09)

c = 0

done = True
listLinesBuffer = []
tabIndexes = [i for i in range(rowRange)]

check = True
turnedOn = True

payload, line2, line = ('', ) * 3

def createPic():
	global turnedOn, payload, line2, line, check

	print("hello from fred")

	curLine = ''

	while True:

		if curLine != line and line != '':
			if len(payload) != 640:
				print('false ' + line)
				continue

				curLine = line
				print(line2 + ' ' + str(len(payload)) )
				# number = line[-1][:-2]
				if int(line2) > 219:
					print('1.' + line + ' ' + line2 + ' ' + str(len(payload)) )
				if int(line2) > 230:
					check = False

			# turnedOn = False

def readLine(name):
	global check, line, payload, line2, turnedOn

	while True:
		if check:
			# print('read')
			try:
				if s.in_waiting > 0:
					buff = s.readline()

					line, payload, line2 = buff.decode("UTF-8").rstrip('\r\n').split(',')
					print(line + " " +name )
				# turnedOn = True
			except:
				continue


# threadDataCollector2 = threading.Thread(target=readLine, args=('two', ))
# threadDataCollector2.start()

# threadDataCollector1 = threading.Thread(target=readLine, args=('one', ))
# threadDataCollector1.start()

# threadDataCollector2 = threading.Thread(target=readLine, args=( ))
# threadDataCollector2.start()

threadPicCreator = threading.Thread(target=createPic, args=( ))
threadPicCreator.start()


tab = [i for i in range(240)]

while check:
	try:
		if s.in_waiting > 0:
			buff = s.readline()

			line, payload, line2 = buff.decode("UTF-8").rstrip('\r\n').split(',')

			row = int(line2)
			
			# tab.remove(int(line[1:]))
			if row in tab:
				tab.remove(row)

			if row == 239:
				print('remaining len: ' + str(len(tab)))
				# for k in tab:
				# 	print(str(k) +',',  end='')

				tab = [i for i in range(240)]

	except Exception as e:
		print(e)
		# print(buff)
		continue

	# if len(payload) != 640:
	# 	continue

	# print(line2 + ' ' + str(len(payload)) )
	# # number = line[-1][:-2]
	# if int(line2) > 219:
	# 	print('1.' + line + ' ' + line2 + ' ' + str(len(payload)) )
	# if int(line2) > 230:
	# 	check = False

# for i in range(30):
			
# 	print(s.readline())


'''

for i in range(0,rowRange):
	if i % 60 == 0:
		print('line {}'.format(i))
	listLinesBuffer.append(s.readline())

print('initial pic array craeted, len: ' + str(len(listLinesBuffer)))
# print(listLinesBuffer[40])


for line in listLinesBuffer:
	try:

		valuesLine = line.decode("UTF-8").rstrip('\r\n').split(',')[1]
	except:
		print(line)
		continue

	size = len(valuesLine)

	if size == 320 * 2:
		lineNumber = int(line.decode("UTF-8").rstrip('\r\n').split(',')[2])
		
		d[lineNumber] = valuesLine

print('pic dictionary created')

# =========================
# DATA gathered, writing to FILE
# =========================

# crete pic list & write data to file
# print(d)

# sorted dict returns indexes
# cast dict to array
for rowIdx in sorted(d):
	try:
		pic[rowIdx] = d[rowIdx]
	except:
		print('index out of index: {}'.format(rowIdx))

	file.write(str(rowIdx) + ',' + d[rowIdx] + '\n')

file.close()
s.close()

print('pic dict sorted and written to file')

sort()
'''

# =========================
# make PIC
# =========================

'''
for row in pic:
	
	# pop frame number if frame not "zero"
	if len(set(row)) != 1:
		row.pop()
	
	tmp = []

	for i in row:
	    for j in re.findall('..', i):
	            tmp.append(int(j, 16))
	    if len(tmp) > 319:
	    	break

	# fill missing data cells with '00'
	r = 320 - len(tmp)

	for i in range(r):
		tmp.append('00')

	# remove pixels if there is overhead
	if len(tmp) > 320:
		for i in range(len(tmp) - 320):
			tmp.pop()

	t.append(tmp)

print('final image created')

plt.imshow(np.array(t, dtype='uint8'), interpolation='nearest', cmap='gray')	
plt.show()


'''









'''
while done:
	strLine = s.readline()

	try:
		listPixValues = strLine.decode("UTF-8").rstrip('\r\n').split(',')
	except:
		continue

	tmp = listPixValues.copy()
	rowNum = 0

	if len(listPixValues) == 82:
		try:
			rowNum = int(listPixValues.pop())
		except Exception as e:
			print('error:\r\n{}\r\n{}'.format(e,listPixValues))
			continue

	if len(tmp) != 81:
		print(tmp)

	# remove index in 1st place of row data
	del tmp[0]


	if rowNum in listLinesToCapture and len(tmp) == 81:
		listLinesToCapture.remove(rowNum)

		if len(listLinesToCapture) < 80:
			done = False

		#  TODO check faulty rows
		if len(tmp) == 81:
			d[rowNum] = tmp
		else:
			print()

	# completness bar, 25 = 100%
	# missingRows = numsLeft.split(',')
	donePercent = int((240 - len(listLinesToCapture))/8)
	remainingPercent = 30 - donePercent
	bar = '\r|' + '[]' * donePercent + '  ' * remainingPercent + '|' + ' ' + str(int(donePercent*3.333)) + '%'

	# print(bar, end = '\r')
	# print(len(missingRows))

'''