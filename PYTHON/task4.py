def odd_position_elements(list_of_number):

	odd_element_storage = []

	for number in range(len(list_of_number)):
		if number % 2 == 1:	
			odd_element_storage.append(list_of_number[number])

numbers_list = [5,4,2,1,6,8,9,66,4,2,3]
print(odd_position_elements(numbers_list))
		