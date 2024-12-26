def largest_number(numbers):
	if (not numbers):	
		return None

	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest
	

list_of_numbers = [33,1,13,42,65,87,27]
print(f"The largest number is: {largest_number(list_of_numbers)}")