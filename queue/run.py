from fixed_queue import FixedQueue

inp = int(input("Enter the cap on the Queue size: "))
queue_obj = FixedQueue(inp)

option = True

while option:
	print("1. View Queue forward")
	print("2. View Queue backward")
	print("3. Push item into Queue")
	print("4. Pop item out of Queue")
	inp = int(input("Enter option: "))
	if inp == 1:
		queue_obj.display_forward()
	elif inp == 2:
		queue_obj.display_reverse()
	elif inp == 3:
		item = input("Enter item to push: ")
		print("Pushed: {0}".format(queue_obj.enqueue(item)))
	elif inp == 4:
		print("Popped: {0}".format(queue_obj.dequeue()))
	else:
		option = False	