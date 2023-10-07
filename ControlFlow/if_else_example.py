# age verification


theater_name = "Malcon Movies"
rated_r_age_limit = 18

print(f"Welcome to our {theater_name} Theater")

user_input = int(input("Enter your age:"))
print(f"Your age is {user_input}")

if user_input >= rated_r_age_limit:
    print("You are eligible for theater")
elif user_input < 18:
    print("You are not eligible for theater. you must be at least 18 to enter this movie")