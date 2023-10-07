# Good Loop
# main_number = 8
# user_inpuut = 0

# while user_inpuut!= main_number:
#     user_inpuut = int(input("Enter a number 0 to 10: "))
#     print(type(user_inpuut))
#     print(f"You entered {user_inpuut}")
#     print(user_inpuut != main_number)
# print("Done")


# given a country print its capital city if its in a given set of data else pront unknow
capitals = {"China": "Beijing", 
            "India": "New Delhi", 
            "United States": "New York",
            "France": "Paris",
            "Germany": "Berlin",
            "Spain": "Madrid",
            "Russia": "Moscow",
            "Japan": "Tokyo",
            "South Korea": "Seoul",
            "Canada": "Ottawa",
            "Brazil": "Brasilia",}

# this while loop will iterate in print each capital city until it matches the given data
user_input = "Japan"
for country, capital in capitals.items():
    print("Current capital: " + country)
    if user_input.lower() == country.lower():
        print(capital)
        break