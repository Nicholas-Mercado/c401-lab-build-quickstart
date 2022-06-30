import os
from messages import opening_msg, closing_msg

def get_path():
    """Returns path to this module"""
    path = str(os.path.dirname(os.path.realpath(__file__)))
    return path

def Main():
    
    file_name = opening_msg()
    
Main()
