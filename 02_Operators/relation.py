
#Realtion operator 

"""

>,>=,<,<=


Chaining of relational operators is possible. In the chaining, if all comparisons
returns True then only result is True. If atleast one comparison returns False then the
result is False
"""

# a=10
# b=20
# print("a > b is ",a>b) # false
# print("a >= b is ",a>=b)  #false
# print("a < b is ",a<b)   #True
# print("a <= b is ",a<=b)  #True





#equality operators:

"""

== , !=

We can apply these operators for any type even for incompatible types also
"""






"""
Logical Operators:
and, or ,not
We can apply for all types.
For boolean types behaviour:
and ==>If both arguments are True then only result is True
or ====>If atleast one arugemnt is True then result is True
not ==>complement
True and False ==>False
True or False ===>True
not False ==>True
For non-boolean types behaviour:
0 means False
non-zero means True
empty string is always treated as False


"""



"""
Bitwise Operators:
We can apply these operators bitwise.
These operators are applicable only for int and boolean types.
By mistake if we are trying to apply for any other type then we will get Error.(Type error)
&,|,^,~,<<,>>
print(4&5) ==>valid
print(10.5 & 5.6) ==>
TypeError: unsupported operand type(s) for &: 'float' and 'float'
print(True & True) ==>valid

& ==> If both bits are 1 then only result is 1 otherwise result is 0
| ==> If atleast one bit is 1 then result is 1 otherwise result is 0
^ ==>If bits are different then only result is 1 otherwise result is 0
~ ==>bitwise complement operator
1==>0 & 0==>1
<< ==>Bitwise Left shift
>> ==>Bitwise Right Shift



print(4&5) ==>4

  100  (binary representation of 4)
& 101  (binary representation of 5)
-----
  100  (result in binary)

"""








"""
Shift Operators:
<< Left shift operator
After shifting the empty cells we have to fill with zero
print(10<<2)==>40
0 0 0 0 1 0 1 0
0 0 1 0 1 0 0 0



>> Right Shift operator 
After shifting the empty cells we have to fill with sign bit.( 0 for +ve and 1 for -ve) 
print(10>>2) ==>2 
We can apply bitwise operators for boolean types also 
print(True & False) ==>False 
print(True | False) ===>True
 print(True ^ False) ==>True 
 print(~True) ==>-2 
 print(True<<2) ==>4 
 print(True>>2) ==>0
"""