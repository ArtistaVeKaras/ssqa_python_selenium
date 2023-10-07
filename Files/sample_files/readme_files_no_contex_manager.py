# example 1 reads the contents of files
sample_file = './sample_files/programming_language_wikipedia.txt'

my_file = open(sample_file, 'r')
content = my_file.read()
my_file.close()
print(content)
my_content_list = content.split('\n')

# example 2
my_file = open(sample_file, 'r')
content = my_file.readlines()
my_file.close()
print(content)

# example 3
my_file = open(sample_file, 'r')
content = my_file.readline()
my_file.close()
print(content)