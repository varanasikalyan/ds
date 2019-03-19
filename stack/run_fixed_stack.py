from os import system
from stack.fixed_stack import FixedStack

def exec_fixed():
	system('cls')
	inp = int(input("Enter the cap on the stack size: "))
	stack_obj = FixedStack(inp)

	option = True

	while option:
		print("1. View Stack")
		print("2. Push item into Stack")
		print("3. Pop item out of Stack")
		print("4. Peek into the Stack")
		print("5. Is Stack empty?")
		inp = int(input("Enter option: "))
		if inp == 1:
			stack_obj.display()
		elif inp == 2:
			item = input("Enter item to push: ")
			print("Pushed: {0}".format(stack_obj.push(item)))
		elif inp == 3:
			print("Popped: {0}".format(stack_obj.pop()))
		elif inp == 4:
			print("Peek: {0}".format(stack_obj.peek()))
		elif inp == 5:
			print(stack_obj.is_empty())
		else:
			option = False

	return	