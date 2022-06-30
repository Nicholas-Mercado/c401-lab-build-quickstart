import os
from messages import opening_msg, closing_msg

def get_path():
    """Returns path to this module"""
    path = str(os.path.dirname(os.path.realpath(__file__)))
    return path

def create_project_file(file_name):
    """Creates project file and folder"""
    os.makedirs(f'{file_name}')
    with open(f'{file_name}/{file_name}.py', 'w') as f:
        pass
        
def create_gitignore():
    """Creates gitignore file from assets"""
    with open(f'{get_path()}/file_schema/get_gitignore.txt', 'r') as input:
        with open("gitignore", "w") as output:
            for line in input:
                output.write(line)

def create_readme():
    with open(f'{get_path()}/file_schema/get_README.txt', 'r') as input:
        with open("README.md", "w") as output:
            for line in input:
                output.write(line)

def create_test_file(file_name):
    os.makedirs(f'test')
    with open(f'test/test_{file_name}.py', 'w') as f:
        pass
    with open('test/__init__.py', 'w') as f:
        pass
def create_venv():
    os.system('python3 -m venv .venv') 

def Main():
    
    file_name = opening_msg()
    create_project_file(file_name)
    create_gitignore()
    create_readme()
    create_test_file(file_name)
    create_venv()
    closing_msg()

Main()
