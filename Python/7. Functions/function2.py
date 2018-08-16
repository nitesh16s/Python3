n = int(input('Enter number of students: '))

def name():
	print(name)

def rollnum():
	print(rollnum)

for i in range(n):
	name = input('Enter name of student' + str(i+1) + ': ')
	rollnum = int(input('Enter rollnum of student' + str(i+1) + ': '))
	name(name)
	rollnum(rollnum)