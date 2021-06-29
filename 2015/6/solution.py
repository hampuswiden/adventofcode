import numpy as np

def solution_part_1():
	f = open("input.txt", "r")
	instructions = f.readlines()

	commands = ["turn on", "toggle", "turn off"]
	grid = np.zeros(shape=(1000,1000), dtype=np.int8)

	for instruction in instructions:
		print(instruction)
		command = None
		for c in commands:
			if c in instruction:
				command = c

		start, end = instruction.split(command)[1].split("through")
		start_x, start_y = start.strip().split(',')
		end_x, end_y = end.strip().split(',')
		start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)

		for x in range(start_x, end_x+1):
			for y in range(start_y, end_y+1):
				# update matrix value depending on command
				if command == "turn on":
					grid[x,y] = 1
				elif command == "turn off":
					grid[x,y] = 0
				elif command == "toggle":
					if grid[x,y] == 0:
						#print("c: 0")
						grid[x,y] = 1
					else: # grid[x,y] == 1
						#print("c: 1")
						grid[x,y] = 0
	# count number of active lights
	rows, columns = grid.shape
	
	active_lights = 0
	for x in range(0, rows):
		for y in range(0, columns):
			if grid[x,y] == 1:
				active_lights += 1
	return active_lights


def solution_part_2():
	f = open("input.txt", "r")
	instructions = f.readlines()

	commands = ["turn on", "toggle", "turn off"]
	grid = np.zeros(shape=(1000,1000), dtype=np.int8)

	for instruction in instructions:
		print(instruction)
		command = None
		for c in commands:
			if c in instruction:
				command = c

		start, end = instruction.split(command)[1].split("through")
		start_x, start_y = start.strip().split(',')
		end_x, end_y = end.strip().split(',')
		start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)

		for x in range(start_x, end_x+1):
			for y in range(start_y, end_y+1):
				# update matrix value depending on command
				if command == "turn on":
					grid[x,y] += 1
				elif command == "turn off":
					grid[x,y] -= 1
					if grid[x,y] < 0:
						grid[x,y] = 0
				elif command == "toggle":
					grid[x,y] += 2

	# count number of active lights
	rows, columns = grid.shape
	
	total_brightness = 0
	for x in range(0, rows):
		for y in range(0, columns):
			total_brightness += grid[x,y]
	return total_brightness


if __name__ == "__main__":
	s = solution_part_2()
	print(s)