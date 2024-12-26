def total_list(number_list):

	total = []
	running_total = 0
	
	for number in number_list:
		running_total += number
	return running_total
				 

list_of_numbers = [4,34,3,54,2,23]
print(f"\nTotal = {total_list(list_of_numbers)}")