import time
import serial
from serial import Serial		#pip install pyserial (not serial)
import os

import re
import numpy as np

from matplotlib import pyplot as plt

from sorter import sort

# TODO 
# check on mcu side whats sent
#  check on python side whats received
# how its parsed and errors catched

rowRange = 240
pic = []
t = []
d = {}
listLinesToCapture = list(range(rowRange))

file = open('data.txt', 'w')

pic = [ ['00' for i in range(320)] for j in range(240)]
s = serial.Serial('COM7', 256000)

c = 0

print('data acquired')

done = True
listLinesBuffer = []

for i in range(0,rowRange):
	if i % 60 == 0:
		print('line {}'.format(i))
	listLinesBuffer.append(s.readline())


print('initial pic array craeted')

for line in listLinesBuffer:
	try:
		values = line.decode("UTF-8").rstrip('\r\n').split(',')
	except:
		print(line)
		continue

	size = len(values)

	if size == 82:
		rownumber = int(values[0][1:])
		# print(rownumber)
		d[rownumber] = values[1:]

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

	line = ''

	for n in d[rowIdx]:
		line += str(n) + ','
	line += '\n'
	file.write(line)


file.close()
s.close()

print('pic dict sorted and written to file')

sort()
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