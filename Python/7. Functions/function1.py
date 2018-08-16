#Make a Calculator in python with function

def add(a,b):
	print(a+b)

def subtract(a,b):
	print(a-b)

def multiply(a,b):
	print(a*b)

def division(a,b):
	print(a/b)

#Two conditions first one is you can give value of a and b in code or second you can take as user input

#In Code

add(2,3)
subtract(3,5)
multiply(2,4)
division(5,2)

#As user input

a = float(input('Enter value of digit1: '))
b = float(input('Enter value of digit2: '))

add(a,b)
subtract(a,b)
multiply(a,b)
division(a,b)