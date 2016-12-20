# Keep track of coordinates with a complex value. why not
import fileinput
import cmath
import re

heading = complex(1+0j)
result = complex()

# Have to go one step at a time and record all locations visited for part 2
locationHistory = [complex(0+0j)]
 
for line in fileinput.input():
	for command in line.split(","):
		steps = int(re.findall('\d+', command)[0])
		if "R" in command:
			heading *= -1j
		else:
			heading *= 1j 
		for step in range(steps):
			result += heading
			if result in locationHistory:
				print(locationHistory)
				print(abs(result.real) + abs(result.imag))
				exit()	
			else:
				locationHistory.append(result)

