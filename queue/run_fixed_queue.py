from os import system
from queue.fixed_queue import FixedQueue

def exec_fixed():
	system('cls')
	inp = int(input("Enter the cap on the Queue size: "))
	queue_obj = FixedQueue(inp)

	option = True

	while option:
		print("1. Push item into Queue")
		print("2. Pop item out of Queue")
		print("3. View Queue forward")
		print("4. View Queue backward")
		inp = int(input("Enter option: "))
		if inp == 1:
			item = input("Enter item to push: ")
			print("Pushed: {0}".format(queue_obj.enqueue(item)))
		elif inp == 2:
			print("Popped: {0}".format(queue_obj.dequeue()))
		elif inp == 3:
			queue_obj.display_forward()
		elif inp == 4:
			queue_obj.display_reverse()		
		else:
			option = False

	return