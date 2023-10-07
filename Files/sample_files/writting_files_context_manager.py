

# writting into a file and a new line after each sentence
my_string = "I love to program in Python language"

# my_f = open('./sample_files/sample_output.txt', 'w')
# my_f.write(my_string)
# my_f.write('\n')
# my_f.write(my_string)
# my_f.write('\n')
# my_f.write(my_string)
# my_f.close()


# ex 2 iterate each item in my_list write and add a new line
# my_list = ['user1', 'user2', 'user3', 'user4']
# with open('./sample_files/sample_output1.txt', 'w') as my_f:
#     for i in my_list:
#         my_f.write(i)
#         my_f.write('\n')

# ex 3 append something to the already existting file
# var = "I love testing in Python language"
# with open('./sample_files/sample_output.txt', 'a') as my_f:
#         my_f.write("\n")
#         my_f.write(var)        

# ex 4 writting into a  csv file swith the join method
my_langs = ['Java', 'PHP', 'Python', 'C++']
with open('./my_fav_languages.csv', 'w') as f:
    str_my_langs = '\n'.join(my_langs)
    f.write(str_my_langs)