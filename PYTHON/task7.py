# Write a function to test weather a string is palindrom

def palindrom(text):
	reverse = users_entry[::-1]

	if text == reverse:
		print(f"{text} is a palindrom")
	else:
		print(f"{text} is not a palindrom")
	return users_entry


users_entry = str(input("Enter a number: ")).strip()

palindrom(users_entry)