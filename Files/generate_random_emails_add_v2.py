"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate-random_email_with_list_of_domains_v1.csv
"""
import random
import string

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

lenght_of_emails = 10 # each email is 10 characters long
total_number_of_emails = 100
output_file = 'output_generate_random_email_with_list_of_domains_v2.csv'
letters = string.ascii_lowercase


# store all emails in a list
all_email =[]
for i in range(100):
    randon_domain = random.choice(list_of_domains)
    random_string = ''.join(random.choice(letters) for i in range(lenght_of_emails))
    rand_email = random_string + '@' + randon_domain
    all_email.append(rand_email)

# print(all_email)    

with open(output_file, 'w') as f:
    f.write(',\n'.join(all_email))
    print()