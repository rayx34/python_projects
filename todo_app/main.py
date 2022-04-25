from tasks import Task

task = Task()
# Print logo
print("\nTODO List")

while True:
	# Ask user what they would like to do display tasks, add, remove or quit app
	print("\nWhat would you like to do?")
	choice = input("Choose from menu below by typing the number:\n1. Display tasks\n2. Add task\n3. Remove task\n4. Quit\n")

	if choice == '1':
		task.display_tasks()
	
	elif choice == '2':
		task.add_task()

	elif choice == '3':
		task.remove_task()

	# Exits program
	elif choice == '4':
		print("Goodbye!")
		exit()

	# Catches invalid entries
	else:
		print("Invalid input. Please choose from the menu by using the number beside it.")