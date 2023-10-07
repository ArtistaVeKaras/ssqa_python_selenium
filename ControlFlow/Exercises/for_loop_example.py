# Example 1
# my_list = ["boat", "cat", "dog", "horse", "sheep"]

# for i in my_list:
#     print(i)
#     print('----------')
    
# Example 2
# quote = "This is going to a very long string that is going to take up more than 100 characters."
# word_list = quote.split() # split the string into a list of words
# print(word_list )
# for i in word_list:
#     if len(i) <=3:
#         print(i)
#         print('----------')


# Example 3
quote = "This is going to a very long string that is going to take up more than 100 characters."
word_list = quote.split() # split the string into a list of words
print("This is my list: {word_list}")
small_list = []
for i in word_list:
    if len(i) >=3:
        small_list.append(i)
        print(small_list)
