"""
If we want to represent a group of values 
without duplicates where order is not important then we should go for "set Data Type".

1. insertion order is not preserved 
2. duplicates are not allowed 
3. heterogeneous objects are allowed 
4. index concept is not applicable 
5. It is mutable collection 
6. Growable in nature

"""

s= {100,0,10,200,20,"Pranav","ALok"}

# print(s)#{0, 100, 20, 'Pranav', 200, 10, 'ALok'}

# print(type(s)) #<class 'set'>

s.add("family")

# print(s) #{0, 100, 20, 'Pranav', 200, 'family', 10, 'ALok'}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# result_set = set1.union(set2)  # or result_set = set1 | set2

# print(result_set)# 
set1.update(set2)

# print(set1)
set1.remove(3)
# print(set1)

# we can see that order is not important






#frozenset Data Type:

"""
It is exactly same as set except that it is immutable. Hence we cannot use add or remove functions.
"""

s = {10,12,13,14,15}
f = frozenset(s)
print(f)   #frozenset({10, 12, 13, 14, 15})


print(type(f)) #<class 'frozenset'>


for i in f : print(i)

# f.add(100)  # Attribute error



