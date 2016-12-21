# Keep track of coordinates with a complex value. why not
import fileinput
import re
from operator import add

keypad = {(-1,1): 1, (0,1): 2, (1,1): 3, (-1,0): 4, (0,0): 5, (1,0): 6, (-1,-1): 7, (0,-1): 8, (1,-1): 9} 
keypress = {'U': [0,1], 'D': [0,-1], 'L': [-1,0], 'R': [1,0]}

keypad2 = {(-1,1): 2, (0,1): 3, (1,1): 4, (-1,0): 6, (0,0): 7, (1,0): 8, (-1,-1): 10, (0,-1): 11, (1,-1): 12, (0,2): 1, (-2,0): 5, (2,0):9, (0,-2):13} 
keypress2 = {'U': [0,1], 'D': [0,-1], 'L': [-1,0], 'R': [1,0]}


for line in fileinput.input():
	location = [-2,0]
	for c in line:
		if c not in keypress2.keys():
			continue
		newLocation = list(map(add, location, keypress2[c]))
		if tuple(newLocation) in keypad2.keys():
			location = newLocation
	print(keypad2[tuple(location)])

