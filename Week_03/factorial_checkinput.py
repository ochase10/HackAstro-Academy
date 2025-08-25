'''
This program computes the factorial of a user-input number.

Usage: python factorial_checkinput.py 9
'''

#get input from the user
good = False
while not good:
	n = input("Please enter a number: ")
	try:
		n = int(n)
	except:
		continue	
	good = True

#initialize a running product
prod = 1

#loop over range(n) gives 0,1,2,...,n-1
for x in range(n):
	#x+1 because we want to multiply 1,2,3,...,n
	prod *= x+1 

#print the result in a good looking way
print(f"{n}! = {prod}")
