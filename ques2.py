'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''
#!/usr/bin/python3
def fact(x):
	if x==0:
		return 1
	else:
		return x * fact(x-1)
x= int(input("Enter the number: "))
print(fact(x))
