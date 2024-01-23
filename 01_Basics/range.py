

#Range dataType

"""
range Data Type represents a sequence of numbers. 
The elements present in range Data type are not modifiable. 
i.e range Data type is immutable.
"""

#'range' object does not support item assignment (means we can not add or remove any value from it)

# print(range(10))#range(0, 10)

r = range(10)
for i in r: print(i) #print 0 to 9


r1 = range(10,20,2)
for i in r1: print(i) # 10,12,16,18

# We can access the element by reference
print(r1[2]) # 14  


l = list(range(10))

print(l)





