import hashlib

def solution_part_1():
	f = open("input.txt", "r")
	key = f.read().strip()

	number = 1
	my_str = key + str(number)
	md5_sum = hashlib.md5(my_str.encode('utf-8')).hexdigest()
	while md5_sum[0:5] != "00000":
		print(number)
		number += 1
		my_str = key + str(number)
		md5_sum = hashlib.md5(my_str.encode('utf-8')).hexdigest()

	print("md5(" + str(my_str) + ") = " + md5_sum)
	return number

def solution_part_2():
	f = open("input.txt", "r")
	key = f.read().strip()

	number = 1
	my_str = key + str(number)
	md5_sum = hashlib.md5(my_str.encode('utf-8')).hexdigest()
	while md5_sum[0:6] != "000000":
		print(number)
		number += 1
		my_str = key + str(number)
		md5_sum = hashlib.md5(my_str.encode('utf-8')).hexdigest()

	print("md5(" + str(my_str) + ") = " + md5_sum)
	return number

if __name__ == "__main__":
	s = solution_part_2()
	print(s)