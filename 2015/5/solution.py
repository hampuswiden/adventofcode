
def solution_part_1():
	f = open("input.txt", "r")
	strings = f.readlines()

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	nice_strings = 0
	for string in strings:
		string = string.strip()

		forbidden_substrings = ["ab", "cd", "pq", "xy"]
		vowels = 0
		double_character = False
		forbidden = False
		for i, c in enumerate(string): # vowels
			if c in "aeiou":
				vowels += 1
			if i < len(string)-1 and c == string[i+1]: # double character
				double_character = True

		for forbidden_substring in forbidden_substrings:
			if forbidden_substring in string:
				forbidden = True		#print("Vowels: " + str(vowels) + ", double_character " + str(double_character) + ", forbidden_sub: " + str(forbidden))
		if vowels >= 3 and double_character and not forbidden:
			nice_strings += 1
	return nice_strings


def solution_part_2():
	f = open("input.txt", "r")
	strings = f.readlines()

	nice_strings = 0
	for string in strings:
		string = string.strip()

		repeated_pair = False
		one_space_between = False
		for i in range(0, len(string)):
			if i < len(string)-2:
				pair = string[i:i+2]
				if pair in string[i+2:]:
					repeated_pair = True

				if string[i] == string[i+2]:
					one_space_between = True

		if repeated_pair and one_space_between:
			nice_strings += 1
	return nice_strings


if __name__ == "__main__":
	s = solution_part_2()
	print(s)