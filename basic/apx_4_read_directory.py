import os, sys

# get all the python path
c = sys.path
print c

# append path to the sys.path
sys.path.append("/home/me/mypy")

# read all the file in this directory
f = os.listdir('C:\Users\Paolo\Desktop\corso_rhino_python')
print f