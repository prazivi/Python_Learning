
#Byte 

# bytes data type represents a group of byte numbers just like an array. 
# But the allowed values are only 0 to 256, if we try 257 then we will get valueerror
# we can not modify value in Byte datatype.

# x = [10,20,30,40];
# b = bytes(x);
# print(b[0]) #10
# print(b[-1]) #40
# print(b[2]) #30

#Once we creates bytes data type value, we cannot change its values,otherwise we will get TypeError.


#Bytearray

# bytearray is exactly same as bytes data type except that its elements can be modified.

# x = [10,20,30,40]
# b= bytearray(x)
# print(b[0]) #10

# b[3]=100

# for i in b :
#     print(i)


# x1 = [10,255] #if 256 then we will get Valueerror
# b = bytearray(x1)
# for i in b :
#     print(i)




