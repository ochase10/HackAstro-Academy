#get input from user
n = int(input("Please enter a number: "))

#initialize running product
prod = 1

#start a counter
i = 1

#loop while i<=n
while (i<=n):
	prod *= i
	i+=1

print(f"{n}! = {prod}")
