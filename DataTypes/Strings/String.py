# myString = "Hello World"

# print(myString.upper())
# print(myString.lower())
# print(myString.strip())
# print(myString)
# print(myString.split('-'))
# print(myString.count('H')) # counts the number of 'H' included in the string
# print(len(myString))

# print('================================')

# ssn = "123-33-777"
# print(ssn)
# print(ssn.split("-"))

# url = "http://www.example.com"
# is_url = url.endswith('.shop')
# print(is_url)

# string slippitng
print('================================')

info = "This20%is20%your20%url20%endocde"
info2 = info.replace('20%', ' ')
print(info)
print(info2)

# String formatting
print('================================')
prg = "Java"
myVar  = "I love {} progamming language".format("Python")
myVar1 = "{} is {}".format("Akiira", 39)
myVar2 = f"I love {prg} programming language"
print(myVar)
print(myVar1)
print(myVar2)