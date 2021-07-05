import hashlib

My_string = input('Enter String to hash:')
result = hashlib.md5(My_string.encode())
print("the equivalent of My_string hash is =",end="")
print(result)