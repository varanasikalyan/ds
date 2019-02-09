from stack.run_fixed_stack import exec_fixed as stack_fixed
from queue.run_fixed_queue import exec_fixed as queue_fixed

option = True

while option:	
	print("1. Fixed Stack")
	print("2. Stack")
	print("3. Fixed Queue")
	print("4. Queue")
	inp = int(input("Enter option: "))
	if inp == 1:
		stack_fixed()
	elif inp == 2:
		stack_fixed()
	elif inp == 3:
		queue_fixed()
	elif inp == 4:
		queue_fixed()		
	else:
		option = False