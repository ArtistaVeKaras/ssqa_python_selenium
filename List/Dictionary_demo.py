# Another example of dictionary

employee = {"name": "John",
            "phone": 555-555-5555,
            "email": "demo@example.com",
            "title": "Developer",
            "skills": ["Python", "Java", "Docker"],
            "salary": 10000.00}

print(employee)

username = employee['name']
useremail = employee['email']
usertitle = employee['title']
userskills = employee['skills']
print(f" The user's name is {username}, user's email is {useremail} and user's title is {usertitle} ")