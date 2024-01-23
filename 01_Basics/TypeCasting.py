"""
We can convert one type value to another type. This conversion is called Typecasting or Type coersion. The following are various inbuilt functions for type casting.
1. int() 
2. float() 
3. complex() 
4. bool() 
5. str()
"""
# int()
# print(int(123.45)) #123

#print(int(10+5j)); # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# print(int("10")) #10

# print(int("10.5"))  #ValueError: invalid literal for int() with base 10: '10.5'



# float()


# print(float(10))#10.0
# print(float("10"))#10.0
# print(float("10.4"))#10.4



# complex()

# We can use complex() function to convert other types to complex type


#complex(x)


# print(complex(10))#(10+0j)
# print(complex(10.4))#(10.4+0j)
# print(complex("10.5"))#(10.5+0j)


# complex(x,y)

# print(complex(2,3))#(2+3j)
# print(complex("10",3))#TypeError: complex() can't take second arg if first is a string
# print(complex(True,False))#(1+0j)




#bool()


# We can use this function to convert other type values to bool type.

print(bool("1"))#True
print(bool("10.5"))#True
print(bool("true"))#True
print(bool(0+1.5j))#True
print(bool(""))#false





