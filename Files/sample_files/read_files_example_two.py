
import pdb

country_file = './sample_files/programming_list_of_contries.txt'
with open(country_file, 'r') as my_f:
    countries= my_f.read()
    
    pdb.set_trace()
    
    
    # run this in the pdb terminal
    # list_of_contries = countries.split('\n')
    # list_of_contries 