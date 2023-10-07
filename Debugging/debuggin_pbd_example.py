import pdb

""" demo 1 
c = continue
n = next
l = show current line
s = step
h= help
pp= pretty print
"""

# print("Testing with pdb")
# fname = "Admas"
# lname = "Correct"

# pdb.set_trace()

# print("I am in the second line")
# print("I am in the third line")
# print(f"first name {fname}, second name {lname}")



def get_user_name(name):
    user_names = {"admas": "ak",
                 "joe": "joe99",
                 "mary": "marryocks2020"}

    # print(f'The user "{user_names[name]}" is logged in')             

    return user_names[name]

    
user_1 = get_user_name("admas")    
print("User 1:" +user_1)
pdb.set_trace()

user_2 = get_user_name("joe")
print("User 2:" +user_2)