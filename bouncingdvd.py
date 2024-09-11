import random,sys,time

try:
	import bext

except ImportError:
	sys.exit()


width, height = bext.size()

colors = ['Red','Blue', 'Yellow','Green','Orange']

right_down = 'rd'
left_dowm = 'ld'
right_up = 'ru'
left_up = 'lu'
directioins = [right_down, left_dowm,right_up,left_up]
