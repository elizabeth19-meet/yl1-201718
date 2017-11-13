def f(list):
	return [list[0],list[-1]]

a=[1,2,3,4]
a.append(6)
print(f(a))





b=[12, 5, 24, 3, 17]
def printLessThan5(b):
	for value in b:
		if value < 5:
			print(value)

printLessThan5(b)

def lessThanInput(list1):
	number = input("What number do you wish to choose? ")
	newList=[]
	for i in b:
		if i<5:
			newList.append(i)
	return newList