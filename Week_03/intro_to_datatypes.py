#There are various common data types in Python. These include int, float, string, boolean, and list.
#Python is a dynamically-typed language. That means that Python determines data types at run time and a variable can
#change type. This makes programming easier because we don't have to specify what type our variable is.
#However, we should keep track of what type our variables are since the methods avaialable to our variables
#is type-dependent.

a = 5 #Python will make interpret this as an int (a small-ish value with no decimal places)
print(type(a))

b = 10.1 #Python will interpet this as a float (for larger numbers and any decimals)
print(type(b))

c = 5. #This will be interpreted as a float. This is one way to force Python to make a variable a float even if the number
print(type(c))        # has no decimal places

d = True #a boolean
print(type(d))

e = [a, b, c, d] #A list. Note the square brackets. Also notice that lists do not have to have a uniform type
print(type(e))


a = 9.3 #Notice that Python will allow me to change the type of 'a'
print(type(a))


#Conversion of Data Types in Python
#You can usually convert one data type to another using the respective 
#Python syntax for that data type. Not all types are convertible
#Let's see some examples below

float_to_int = int(3.14159)
int_to_float = float(3)
int_to_string = str(3)
float_to_string = str(3.14159)
string_to_int = int('3')
string_to_float = float('3.14159')
int_to_bool = bool(0)
float_to_bool = bool(0.0)
string_to_bool = bool('False')

# list_to_int = int([1,2,4]) This will fail!

###############
#Strings
##############
#The + and * methods have string implementations

print('Hello' + 'World')

print('Hello' + ' ' + 'World')

print('Hello' * 4)


################
# Some useful string methods
################
#.upper() and .lower() are string methods to change the case of the whole string

string1 = 'hello world'
upper_string = string1.upper()
print(upper_string)
lower_string = upper_string.lower()
print(lower_string)

############
#replace method
############
#the .replace() method swaps any pattern into something different. If the pattern doesn't exist, nothing happens.
#Note that it changes all occurances of the pattern, not just the first.

replace_world = string1.replace('world', 'universe')
print(replace_world)

replace_world = string1.replace('hello', 'cool')
print(replace_world)

#############
#split method
#############
#.split() is a very useful string method that allows you to break up a string into chunks using any 
# character as a delimiter

long_sentence = 'This is a long sentence that we will split into words'
split_sentence = long_sentence.split()
print(split_sentence)

file_path = 'C:/Users/username/Documents/Python/Week_03/intro_to_datatypes.py'
split_path = file_path.split('/')
print(split_path)

split_path_underscore = file_path.split('_')
print(split_path_underscore)


#The psudo-inverse of .split() is .join()
#Note that .join is operating on the delimiter not the string itself
print('/'.join(split_path))
print('**'.join(split_path))


#f-string
#f-strings are a way to format strings in python
#Syntax is f'{variable_name}'
fstring1 = f'I was born in {1995}'

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

#you can also change mutliple entries in one line using slicing

#changes 2nd - 4th item in list to 567
first_list[1:4] = 567

#negative Indexing
last_item = first_list[-1]
print(last_item)

second_to_last = first_list[-2]
print(second_to_last)

last_4_values = first_list[-4:]
print(last_4_values)

every_other_value = first_list[::2]
print(every_other_value)


#Tuples
#Very similar to List
#Access data in much the same way
#slicing applies
#they are immutable, meaning once you make them you cannot change them

first_tuple = (1, 2, 3, 4, 5, [3, 2, 4, 5], True, False, 3.454, (1, 4, True, 'String'))

#try running the code below

first_tuple[5] = 100
first_tuple[-4] = [1, 2, 3, 4, 5]

# 3. Dictionaries
#Differ from list and tuples by not using index to access data but a key-value pairing
#For every key there is one item for that key
#can store a wide range of data types
#not stored in a particular order
#cannot use slicing
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
import numpy
print(f'This is a NaN: {numpy.nan}')
print(f'This is an Infinity: {numpy.inf}')
