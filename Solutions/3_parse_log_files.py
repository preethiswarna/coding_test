# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:56:42 2021

@author: preet
"""

import sys

def parse_log_file(input_file_path):
    '''Extracts error and warnings to specified file
    '''
    output_file_path = r'C:\Users\preet\OneDrive\Desktop\error_info.txt'
    
    # Read log file
    try:
        with open(input_file_path,'r') as log_file:
            log_file_contents = log_file.readlines()
            out_lines = []
            for line in log_file_contents:
                if ("error" in line.lower()) or ("warning" in line.lower()):
                    out_lines.append(line)         
    except:
        print("Unable to access {}".format(input_file_path))
        sys.exit()
        
    # Write extracted info to output file    
    try:
        with open(output_file_path,"a") as out_file:
            out_file.writelines(out_lines)
    except:
            print("Unable to access {}".format(output_file_path))
            sys.exit()
    
    return "Parsed successfully"
                
input_file_path = r'C:\Users\preet\OneDrive\Desktop\log_file.txt'
print(parse_log_file(input_file_path))