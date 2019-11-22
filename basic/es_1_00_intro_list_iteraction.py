value = 10

a_list = [4, 5, 7, ['a', 10.5, "ciao"], 8, 10, 100, 1000, 56]
# print(a_list[0])

# a_list[0] = '5'
# print(a_list)

# test = range(5)
# test = range(10, 0, -2)
# print(test)
# print( type(test) ) 

list_of_values = range(1, 8, 2)
print(list_of_values)

"""
for value in list_of_values:
    print(value)
"""

print("la lista e\' lunga " + str( len(a_list) ) )

for i in range(5):
    print(i)

for value in list_of_values:
    print("Position: " + str(value) )
    print( a_list[value] )


print( range( len(a_list) ) )

j = 0
incr = 1
while j < len(a_list):
    print(j)
    print( a_list[j] )
    j += incr
    # j = j + incr

