# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:00:13 2021

@author: preet
"""

import sys

class Path:
    
    def __init__(self,path):
        self.path = path
        
    def cd(self,new_path):
        if ".." in new_path:
            parent_dir = '/'.join(list(self.path.split('/')[:-1]))
            new_dir = '/'.join([parent_dir,new_path.split('/')[1]])    
        else:
            new_dir = new_path          
        if new_dir.replace('/','').isalpha():
            self.path = new_dir
        else:
            print("Path cannot be changes, invalid charcaters in new path")
            sys.exit()
        
    def current_path(self):
        return self.path
    

path = Path('/a/b/c/d')
print(path.current_path())
path.cd('../x')
print(path.current_path())
path.cd('/a/b/1')
print(path.current_path())