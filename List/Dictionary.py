meal = {"breakfast":  "eggs",  "lauch": "salad"}

mybreakfast = meal["breakfast"]
print("================================")
print(mybreakfast)

# add dinner to the dictionary
meal["dinner"] = "pizza"
print(meal["dinner"])
print(meal)

#Dictionary 
capitals = {"NYC": "New York", "LA": "Los Angeles", "CA": "San Francisco",}
print(type(capitals))

# getting items from dictionary
newyork_capitals = capitals["NYC"] # method one
newyork_capitals2 = capitals.get("LA") # method two
print(newyork_capitals)
print(newyork_capitals2)

# #if value is not found in dictionary print None
london_cap = capitals.get("London", None)
print(london_cap)

#adding items to dictionary
print(capitals)
print("Before add ")
capitals["Kenia"] = "Nairobi"
print("After add ")
print(capitals)

# Assignment: add a value that already exists to the dictionary
# nothing happens nor errors is returned
capitals["NYC"] = "New York"
print(capitals)

# Assignment2: look up what does the method setDefualt() do
# prints the value of the specifiedd key
x = capitals.setdefault("CA", "San Franco")
print(x)
