# Example funstions for adding two numbers

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b    

my_number = add(1, 2)
print(my_number)


def state_has_no_sales_tax(state):
    
    states_with_no_sales_tax = ['AB', 'AL', 'AR', 'AZ', 'AK', 'CL', 'CC']
    
    if state.upper() in states_with_no_sales_tax:
        return True
    else:
        return False

user_state = input("What is your state? ")
print(state_has_no_sales_tax(user_state))