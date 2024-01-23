"""
tuple data type is exactly same as list data type except that it is immutable.i.e we cannot chage values.
Tuple elements can be represented within parenthesis.


Note: tuple is the read only version of list
"""
# l = [10,12,23,10]
# print(type(l)) #<class 'list'>

t = (10,12,23,10)
print(type(t)) #<class 'tuple'>

print(t[0]) #10
# t[0]=100 #TypeError: 'tuple' object does not support item assignment

# t.append(100) #AttributeError: 'tuple' object has no attribute 'append'
print(t)




