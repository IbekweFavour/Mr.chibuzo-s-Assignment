
list_of_numbers = [4, 21,2,3,4,5,66]

def element_occurance(numbers):

	number_entered = int(input("Enter a number: "))
	if number_entered in list_of_numbers:
		return "The number is in the list"
	elif number_entered not in list_of_numbers:
		return "The number is not in the list"

print(element_occurance(list_of_numbers))