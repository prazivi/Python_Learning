

#list datatype

"""

If we want to represent a group of values as a single entity where insertion 
order required to preserve and duplicates are allowed then we should go for list data type.
1. insertion order is preserved 
2. heterogeneous objects are allowed 
3. duplicates are allowed 
4. Growable in nature 
5. values should be enclosed within square brackets.
"""

list = [100,"pranav",10.5,100,10+1j,True]
print(list)

# for i in list : print(i);


list.append('Shalini')
print(list)


#An ordered, mutable, heterogenous collection of eleemnts is nothing but list, where duplicates also allowed.