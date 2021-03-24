# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:54:01 2021

@author: preet
"""


def group_of_owners(file_owners_dict):
    '''Returns a dict containing list of file names for each owner.
        Parameters (dict) : A dictionary
        Returns (dict) : A dictionary'''
    group_of_owners = {}
    for key,value in file_owners_dict.items():
        if value in group_of_owners:
            group_of_owners[value].append(key)
        else:
            group_of_owners[value] = [key]
    return group_of_owners
    
input_dict = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
print(group_of_owners(input_dict))