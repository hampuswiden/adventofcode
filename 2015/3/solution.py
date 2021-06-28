
def solution_part_1():
	f = open("input.txt", "r")
	directions = f.read().strip()

	x = 0
	y = 0
	visited_houses = set()
	visited_houses.add(str(x)+","+str(y))
	
	for direction in directions:
		if direction == '^':
			y += 1
		elif direction == 'v':
			y -= 1
		elif direction == '>':
			x += 1
		elif direction == '<':
			x -= 1
		else:
			print(direction)
			return None
		#print(x,y)
		visited_houses.add(str(x)+","+str(y))
	return len(visited_houses)




def solution_part_2():
	f = open("input.txt", "r")
	directions = f.read().strip()

	santa_x = 0
	santa_y = 0
	robo_santa_x = 0
	robo_santa_y = 0
	visited_houses = set()
	visited_houses.add(str(santa_x)+","+str(santa_y))
	
	for i, direction in enumerate(directions):
		if i%2 == 0: # santas turn to move!
			if direction == '^':
				santa_y += 1
			elif direction == 'v':
				santa_y -= 1
			elif direction == '>':
				santa_x += 1
			elif direction == '<':
				santa_x -= 1
			else:
				print(direction)
				return None
			visited_houses.add(str(santa_x)+","+str(santa_y))
		else: # robo santas turn to move
			if direction == '^':
				robo_santa_y += 1
			elif direction == 'v':
				robo_santa_y -= 1
			elif direction == '>':
				robo_santa_x += 1
			elif direction == '<':
				robo_santa_x -= 1
			else:
				print(direction)
				return None
			visited_houses.add(str(robo_santa_x)+","+str(robo_santa_y))
	return len(visited_houses)

if __name__ == "__main__":
	s = solution_part_2()
	print(s)