#The students can use this as a reference as they go through the Python Basics

#importing the numpy package as we need that to go over NaN and Inf
import numpy as np

#Introduce a comment, if the other instructor did not do so already
#This is a comment, use the # symbol to write a comment

#There are 4 data types

#integers

print(1)

print(100)

print(-9)


#floats

print(3.14159)

print(2.99e30)

#Boolean

print(True)

print(False)

#Strings
#To start a string we can use 'STUFF_HERE' or "STUFF_HERE"

print('This is an example of a string')

print('So is this')


#Introducing the Type Function
#The type function will tell you what data type a variable is
print(f'1 is of Type: {type(1)}')
print(f'3.14159 is of Type: {type(3.14159)}')
print(f'True is of Type: {type(True)}')
print(f"Hello is of Type: {type('Hello')}")


#Conversion of Data Types in Python
#You can always convert one data type to another using the respective 
#python syntax for that data type, let's see some examples below

float_to_int = int(3.14159)
int_to_float = float(3)
int_to_string = str(3)
float_to_string = str(3.14159)
string_to_int = int('3')
string_to_float = float('3.14159')
int_to_bool = bool(0)
float_to_bool = bool(0.0)
string_to_bool = bool('False')

#Cases where the conversion will not work
#Converting a string to an integer or float will not work if the string is not a number

str_to_int = int('Hello')

###############
#Strings
##############

print('Hello' + 'World')

print('Hello' + ' ' + 'World')

print('Hello' * 4)

#f-string
#f-string is a way to format strings in python
#syntax is f'{variable_name}'
fstring1 = f'I was born in  {1995}'

mass = 10
fstring2 = f'The mass of the object is log10({mass})'

long_decimal = 3.14159265358979323846264338

fstring3 = f'The value of pi is {long_decimal}'
fstring4 = f'The value of pi is {long_decimal:.2f}'
fstring5 = f'The value of pi is {long_decimal:.8f}'

exponential = 2.8763546382e30
fstring6 = f'The value of the exponential is {exponential:.2e}'
fstring7 = f'The value of the exponential is {exponential:.4e}'


#Below we will outline some of the Python containers, 
#what they are and how to access the data that they hold

#Many different types of Containers

# 1. List
#Lists can hold a variety of data types, even other containers
#Lists keep the order that you created them in
#Can access data using the index 
#Can also change the values if needed

first_list = [12, 34, 'String Here', True, False, 3.14159]

#nested List

nested_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], True, False, 'Another String']

#Access data very similar to strings, we pass in the index of the data we want to grab

print(first_list[0]) #Grabs the first data entry 12

print(first_list[2]) #Grabs the 3rd data entry "String Here"

#changes first entry in first_list from 12 to 100
first_list[0] = 100

#you can also change mutliple entries in one line using splicing

#changes 2nd - 4th item in list to 567
first_list[1:4] = 567

#negative Indexing
last_item = first_list[-1]
print(last_item)

second_to_last = first_list[-2]
print(second_to_last)

last_4_values = first_list[-4:]
print(last_4_values)


#Tuples
#Very similar to List
#Access data in much the same way
#splicing applies
#they are immutable, meaning once you make them you cannot change them

first_tuple = (1, 2, 3, 4, 5, [3, 2, 4, 5], True, False, 3.454, (1, 4, True, 'String'))


# 3. Dictionaries
#Differ from list and tuples by not using index to access data but a key-value pairing
#For every key there is one item for that key
#can store a wide range of data types
#not stored in a particular order
#cannot use splicing
#value for the key can be changed

grocery_dictionary = {'Eggs': 12, 'Milk':2, 'Cereal':1, 'Apples': 4, 'Ice-Cream': 1}

#accessing items in the grocery_list requires the key, in this case Eggs, Milk, Cereal, Apples, Ice-Cream

print(grocery_dictionary['Eggs'])

print(grocery_dictionary['Milk'])


#changing Eggs to 2
grocery_dictionary['Eggs'] = 2

general_dictionary = {'Mass': [8.4, 10.3, 11.1, 7.5, 8.7], 
                      'Velocity': [3.4, 4.5, 5.6, 6.7, 7.8], 
                      'Acceleration': [9.8, 8.7, 7.6, 6.5, 5.4], 
                      'Galaxy_Type': ['Spiral', 'Elliptical', 'Irregular', 'Spiral', 'Elliptical'], 
                      'Massive': [True, False, True, True, False]}

#Introducing NaNs and Infs
print(f'This is a NaN: {np.nan}')
print(f'This is an Infinity: {np.inf}')
