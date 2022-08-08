import pandas as pd
import numpy as np

def remove_nonnumericals(string):
    # string is the string from which non-numerical characters need to be removed
    
    string_list = string.split()  # convert single string into a list.
    
    # see ** below for explanation of nested list comprehension
    numeric_list = [''.join([char for char in element if (char.isdigit() or char=='.')]) for element in string_list]
    
    # see *** below for explanation
    return [float(element) for element in list(filter(None, numeric_list))]