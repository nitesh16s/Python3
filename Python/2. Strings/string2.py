#loops with strings

n = int(input('Enter number of students: ')) #Use int before taking user unput in an integer form.

for index in range(n):
	student = input('Enter name of student' + str(index+1) + ': ')
	rollnum = int(input('Enter roll.no of student' + str(index+1) + ': '))
	print('Name: ', student + ' | ' + 'Roll.No: ', rollnum)

print('\n')
print('Do some effort for better.')
print('Good Bye!')
print('Happy Coding!')