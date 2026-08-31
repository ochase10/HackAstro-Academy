####
# This file contains a function for generating random numeric lists
# 
# Edited: 9/2/25
#
# Author: Owen Chase
####

from random import random

def generate_list(n=None):
    '''
    Function for generating random list of integers of random or specified length

    Arguments:
        - n: (int) Length of returned list, if None a random length is generated
                   between 10 and 10,000

    Return:
        - newlist: (list) List of length n
    '''

    if n is None:
        n = int(random() * 9990 + 10)

    newlist = []

    for i in range(n):
        # Each element of newlist will be an integer between -1,000,000 and 1,000,000
        newlist.append(int(random() * 2000000 - 1000000))

    return newlist


if '__name__' == '__main__':
    print("This file does not currently have a main function implemented")