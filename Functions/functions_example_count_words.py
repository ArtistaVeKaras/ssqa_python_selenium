
def get_count_of_small_words(input_string, max_size=3): #max size is the default value and you don't need to call it

    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)
            
    return len(small_words)

my_joke = "Just type any random word in the input string and return what you want in the current terminal"       

# the above prnt they all valid
num_samll = get_count_of_small_words(my_joke)
num_samll_1 = get_count_of_small_words(my_joke, max_size=4)
num_samll_2 = get_count_of_small_words(my_joke, 4)
print(num_samll_1)


def connect_to_database(host='test.db.com', usernamr='testuser', password='secret'):
    print(f"Connection to host: {host}")
    print(f"Username: {usernamr}")

    
connect_to_database(host='probdb.com', usernamr='myproduser', password='secret')    
connect_to_database('probdb.com', 'myproduser', 'secret')    # they both do the same thing but in this line we don't need to specifi the variable