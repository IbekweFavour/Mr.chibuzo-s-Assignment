number1 = int(input("Enter a number: "))
number2 = int(input("Enter the second number: "))


if (number1 > number2):
	number2 = number1
	print(f"The greatest number is: {number2}")
elif (number2 > number1):
	number1 = number2
	print(f"The greatest number is: {number1}")