print("What's your name?")
name = input("Type your name here: ")
if name.isalpha():
	print("What year were you born? ")	
	byear = input("Type your birth year here: ")
	try:
		byear_as_int = int(byear)
		age = 2026 - byear_as_int
		if age > 100:
			print("It's unlikely you're over 100 years old. Input your real birthyear please.")
		else:
			if age < 1:
				print("I don't think you're old enough to type yet, or perhaps exist? Input your real birthyear please.")
			else:
				print(f"Hello, {name}! You are {age} years old.")
	except ValueError:
		print("Please input your birth year as an integer.")
else:
	print("Please input your name with only alphabet characters.")
