number_list = [2,3,1,4,4,5,6,6,7,3,8,23,4,3,44,6,777,433]

def odd_position(numbers):
	for number in numbers:
		if (number % 2 == 1):
			return number
		else:
			return "There is no odd number in the list"

print(odd_position(number_list))
	