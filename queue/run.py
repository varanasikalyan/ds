from fixed_queue import FixedQueue

inp = int(input("Enter the cap on the Queue size: "))
queue_obj = FixedQueue(inp)

option = True

while option:
	print("1. View Queue")
	print("2. Push item into Queue")
	print("3. Pop item out of Queue")
	print("4. Peek into the Queue")
	print("5. Is Queue empty?")
	inp = int(input("Enter option: "))
	if inp == 1:
		queue_obj.display()
	elif inp == 2:
		item = input("Enter item to push: ")
		print("Pushed: {0}".format(queue_obj.push(item)))
	elif inp == 3:
		print("Popped: {0}".format(queue_obj.pop()))
	elif inp == 4:
		print("Peek: {0}".format(queue_obj.peek()))
	elif inp == 5:
		print(queue_obj.is_empty())
	else:
		option = False	