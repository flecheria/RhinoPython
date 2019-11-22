import rhinoscriptsyntax as rs

"""
test_str = "casa"
print( test_str.capitalize() )
"""

test_str = "this is a string"
test_str_1 = "THIS IS ALL UPPERCASE"
test_str_2 = "this is, a string"

macro_test = "_Line 0,0,0 0,0,0"

print( test_str.count("is") )
print( len(test_str) )
print( test_str.upper() )
print( test_str_1.lower() )

print( test_str.split() )

print( test_str_2.split(',') )

test = macro_test.split()
print(test)

point_a = ['10,0,0', '20,0,0', '30,0,0']
point_b = ['50,80,0', '60,80,0', '120,240,56']

# print( test_str.replace("string", "not a string") )

"""
for i in range( len(point_a) ):
    command = test[0] + ' ' + point_a[i] + ' ' + point_b[i]
    # DEBUG
    print(command)
    rs.Command(command)
"""

# test_str = "this is a string"
index_1 = test_str.find(' ')
index_2 = test_str[::-1].find(' ')
print(test_str[::-1])
print( test_str[index_1: len(test_str) - index_2] )