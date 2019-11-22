l_test = ["paolo", 2, 10.56, [7, 7, 8], "ugo"]

print(l_test[2])
print( len(l_test) )

print( l_test[1:3] )
print( l_test[2: ] )
print( l_test[ :2] )
print( l_test[::-1] )
print(l_test)

bbox = [1000, 500, 100]

bbox_exp = [bbox[1], bbox[0], bbox[2]]


print( l_test.append('cippo') )
print(l_test)
l_test[1] = 2354892
print(l_test)

print( l_test[3][1] )