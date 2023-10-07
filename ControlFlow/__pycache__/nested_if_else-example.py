# age verification example 2
theater_name = "Malcon Movies"
rated_r_age_limit = 18

print(f"Welcome to our {theater_name} Theater")

user_input = int(input("Enter your age:"))
print(f"Your age is {user_input}")

if user_input >= rated_r_age_limit:
    print("Enjoy  the movie")
else:
    adul_present = input("Is an adult present with you? yes or no: ")
    if adul_present.lower() == "yes":
        print("Enjoy  the movie")
    else:
        print("you must be at least 18")