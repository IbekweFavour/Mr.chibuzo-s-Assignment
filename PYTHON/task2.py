reversed_ = []


def reverse_list(number_list):

	for number in number_list:
		reversed_.insert(0, number)
	return reversed_

list_of_numbers = [1,2,3,4,5,6]
print(f"The original list is: {list_of_numbers}")
print(f"The reversed list is: {reverse_list(list_of_numbers)}")