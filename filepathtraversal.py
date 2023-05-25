import os
import re
import sys
def main():
    filename = sys.argv[1]
    
    #if you want to implement the code with error put the comment line on the error solved and vice versa
    
 #with error
    
    #path = os.path.join(os.getcwd(), filename)
    
#error solved
    
    filename = re.findall('[\\/]*([a-zA-Z0-9]+[.][a-zA-Z0-9]+)$', filename)[0]
    
    
    path = os.path.join(os.getcwd(), filename)
    try:
        print('Reading:', os.path.abspath(path))
        with open(path, 'r') as f:
            file_data = f.read()
            print('File data:', file_data)
    except FileNotFoundError as e:
        print("Error - file not found", e)
main()