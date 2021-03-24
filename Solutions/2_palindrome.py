# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:56:03 2021

@author: preet
"""


def is_palindrome(input_str):
    '''Checks whether given word is plaindrome or not.
        Parameters (str) : Input string
        Returns (str) : A string which tells given word is plaindrome or not '''
    input_str = input_str.lower()
    reverse_string = input_str[::-1]
    if input_str == reverse_string:
        return "Given word {} is palindrome".format(input_str)
    else:
        return "Given word {} is not palindrome".format(input_str)

input_str = 'Madam'
print(is_palindrome(input_str))