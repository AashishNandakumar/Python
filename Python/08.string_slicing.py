# Slicing = create a substring from another string
# indexing[] or sliceObj()
# [start:stop:step]
# [inclusive:exclusive:step]

name = 'aashish nk'

first_name = name[:7]
last_name = name[8:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website = 'http://google.com'
website2 = 'http://wikipedia.com'
# create sliceObj (object) and call slice() function
sliceObj = slice(7, -4, 1)

print(website[sliceObj])
print(website2[sliceObj])  






