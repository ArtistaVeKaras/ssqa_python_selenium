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
import pdb

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

lenght_of_email = 10
letters = string.ascii_lowercase
all_emails = []
output_path = ('generate_random_email_with_list_of_domains_v1.csv')

for domain in list_of_domains:
    for i in range(20):
        randdom_string = ''.join(random.choice(letters) for i in range(lenght_of_email))
        print(randdom_string)
        
        email = randdom_string + '@' + domain
        all_emails.append(email) 
print(all_emails)

# take the list and write file
with open(output_path, 'w') as f:
    for email in all_emails:
        f.write(email)
        f.write(',\n')
        