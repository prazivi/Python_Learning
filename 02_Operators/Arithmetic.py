"""
Operator is a symbol that performs certain operations. Python provides the following set of operators 
1. Arithmetic Operators 
2. Relational Operators or Comparison Operators 
3. Logical operators 
4. Bitwise oeprators 
5. Assignment operators 
6. Special operators
"""




# Arithmetic Operator


"""
1. Arithmetic Operators: 
+ ==>Addition 
- ==>Subtraction 
* ==>Multiplication 
/ ==>Division operator 
% ===>Modulo operator 
// ==>Floor Division operator 
** ==>Exponent operator or power operator
"""


a=10
b=2

print('a+b',a+b)
print('a-b',a-b)
print('a*b',a*b)
print('a/b',a/b)
print('a%b',a%b)
print('a//b',a//b)
print('a**b',a**b)


"""
Note: 
/ operator always performs floating point arithmetic. Hence it will always returns
float value.
But Floor division (//) can perform both floating point and integral arithmetic. If
arguments are int type then result is int type. If atleast one argument is float type then
result is float type.
"""



"""
We can use +,* operators for str type also.
If we want to use + operator for str type then compulsory both arguments should be str
type only otherwise we will get error.

1) >>> "durga"+10
2) TypeError: must be str, not int
3) >>> "durga"+"10"
4) 'durga10'
"""

# print(10/0); # Zero division error





