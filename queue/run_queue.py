from queue import Queue

queue_obj = Queue()

option = True

while option:
	print("1. View Queue")
	print("2. Push item into Queue")
	print("3. Pop item out of Queue")
	inp = int(input("Enter option: "))
	if inp == 1:
		queue_obj.display()
	elif inp == 2:
		item = input("Enter item to push: ")
		print("Pushed: {0}".format(queue_obj.push(item)))
	elif inp == 3:
		print("Popped: {0}".format(queue_obj.pop()))
	else:
		option = False	