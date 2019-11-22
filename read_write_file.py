import os

# print current directory
print( os.getcwd() )

# change directory with error because it doesn't exist
# os.chdir('C:\\ThisFolderDoesNotExist')

# set path
"""
folder = 'Documenti'
file = 'tspline_codici.txt'
print( os.path.join('C:\\Users\\flecheria', folder, file) )
"""

# create a new directory
# give an error if the folder already exist
"""
new = 'test_directory'
os.makedirs( os.path.join('C:\\Users\\flecheria\\Documenti', new) )
"""

# get the absolute path of the 
print( os.path.abspath('.') )

# get True if path is absolute / False if is a relative path
print( os.path.isabs('.') )
print( os.path.isabs( os.path.abspath('.') ) )

# get the file size Kb
path = 'C:\\Users\\flecheria\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\scripts'

print( os.listdir(path) )
# get the file size
print( os.path.getsize('read_write_file.py') )

# check path validity and file type
print( os.path.exists(path) )
print( os.path.isfile(path) )
print( os.path.isdir(path) )