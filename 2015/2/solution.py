
def solution_part_1():
	f = open("input.txt", "r")
	dimensions = f.readlines()

	total_area = 0
	for package in dimensions:
		l, w, h = package.split("x")
		l, w, h = int(l), int(w), int(h)
		area = 2*l*w + 2*w*h + 2*l*h + min(l*w, w*h, l*h)
		total_area += area
	return total_area


def solution_part_2():
	f = open("input.txt", "r")
	dimensions = f.readlines()

	total_length = 0
	for package in dimensions:
		l, w, h = package.split("x")
		l, w, h = int(l), int(w), int(h)
		length = 2*min(l+w, w+h, l+h) + l*w*h
		total_length += length
	return total_length

if __name__ == "__main__":
	s = solution_part_2()
	print(s)