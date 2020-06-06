import logging
import threading
import time


s = '123'
on = True

t = 0

def tasku(name):
	global s
	global on

	while on:
		if s == '1':
			print('tredu {} got it!'.format(name))
			s = ''
			time.sleep(0.1)

def time2():
	global t

	prev, cur = (0, ) *2 

	while True:
		if t % 2 == 0 and t != prev:
			prev = t
			print('time from 2')

def time5():
	global t

	prev, cur = (0, ) *2 

	while True:
		if t % 5 == 0 and t != prev:
			prev = t
			print('time from 5')

def timer():
	global t

	while True:
		t = int(time.time())



timer = threading.Thread(target=timer, args=())
t2 = threading.Thread(target=time2, args=())
t5 = threading.Thread(target=time5, args=())

timer.start()
t2.start()
t5.start()


















# x = threading.Thread(target=tasku, args=('[tst tred]', ))
# x.start()


# while True:
# 	time.sleep(1)

# 	s = '1'
# 	# on = False

# 	# time.sleep(0.5)

# 	# s= '1'

# 	print('s - 1')

# 	time.sleep(2)

# 	s = '12'

# 	print('s - 12')



