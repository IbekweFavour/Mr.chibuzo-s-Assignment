def get_even_position_elements(input_list):
	even_position_elements = []

	for index in range(len(input_list)):
		if index % 2 == 0:
			even_position_elements.append(input_list[index])	return even_position_elements

my_list = [21,34,21,45,66,32,12,56,26,33]

print(get_even_position_elements(my_list))