#get input from the user
n = int(input("Please enter a number: "))

#initialize a running product
prod = 1

#loop over range(n) gives 0,1,2,...,n-1
for x in range(n):
	#x+1 because we want to multiply 1,2,3,...,n
	prod *= x+1 

#print the result in a good looking way
print(f"{n}! = {prod}")
