from os import system
from stack.stack_simple import Stack

stack_obj = Stack()

option = True

while option:
	system('cls')
	print("1. View Stack")
	print("2. Push item into Stack")
	print("3. Pop item out of Stack")
	inp = int(input("Enter option: "))
	if inp == 1:
		stack_obj.display()
	elif inp == 2:
		item = input("Enter item to push: ")
		print("Pushed: {0}".format(stack_obj.push(item)))
	elif inp == 3:
		print("Popped: {0}".format(stack_obj.pop()))
	else:
		option = False	