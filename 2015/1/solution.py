
def solution_part_1():
	f = open("input.txt", "r")
	string = f.read().strip()
	
	floor = 0
	for c in string:
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1
		else:
			print("Error")
			return None
	return floor


def solution_part_2():
	f = open("input.txt", "r")
	string = f.read().strip()
	
	floor = 0
	for i, c in enumerate(string):
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1
		else:
			print("Error")
			return None

		if floor == -1:
			return i+1 # enumerate starts with index 0
	print("Never reach floor -1 (basement)")
	return None

if __name__ == "__main__":
	s = solution_part_2()
	print(s)