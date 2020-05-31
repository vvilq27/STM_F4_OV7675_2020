import time
import serial
from serial import Serial		#pip install pyserial (not serial)
import os

import re
import numpy as np

from matplotlib import pyplot as plt
import pprint

# TODO 
# check on mcu side whats sent
#  check on python side whats received
# how its parsed and errors catched

def sort():

	rowRange = 300
	pic = []
	t = []
	d = {}

	counter = {}

	for i in range(0, 240):
		counter[i] = 0

	with open('data.txt', 'r') as picFile:
		lines = picFile.readlines()
		for fileLine in lines:

			rowNumber, line = fileLine.split(',')

			lineNumbers = []

			for charCounter in range(320):
				strNum = line[charCounter: charCounter+2]
				lineNumbers.append(strNum)

			if len(lineNumbers) == 0:
				print('row is empty, close program')
				return

			# holds groups of four lineNumbers per array
			groupings = []

			# for number in lineNumbers[:len(lineNumbers)-2]:
			# for number in lineNumbers:
			# 	groupings.append([number[i:i+2] for i in range(0, len(number), 2) ])

			# print(groupings)

			# array with all values separated
			row = [0 for i in range(320)]
			rowTmp = []
			# for group in groupings[:80]:
			for num in lineNumbers:
				rowTmp.append(int(num, 16))



			# rowNum = int(lineNumbers[-2])

			# counter[rowNum] = counter[rowNum] + 1

			rowLength = len(rowTmp) - 1

			# invert row
			for i in range(0, rowLength):
				row[i] = rowTmp[rowLength - i]

			d[rowNumber] = row

			pic.append(row)


		# pprint.pprint(counter)

		print(len(pic))
		# print(pic[10])

	plt.imshow(np.array(pic, dtype='uint8'), interpolation='nearest', cmap='gray')	
	plt.show()