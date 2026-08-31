# Script for writing your solution to the week 3 checkpoint. 

###########################################
# Do not edit this portion of the script! #
###########################################
import random

a = []

for i in range(random.randint(7,15)):
    num = round(random.random() * 100 - 30, 2)
    test = random.random()
    if test > 0.3:
        num = int(num)
    elif test < 0.1:
        num = str(num)
    a.append(num)

print(a)


###################################
# Write your code below this line #
###################################

# Your code
