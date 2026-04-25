TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

line = "-" *40


users_and_passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

input_username = input("Please write your username:")
input_password = input("Please write your password:")
print(line)

if users_and_passwords.get(input_username) == input_password:           #If input username and password are correct the program continues
    print(f"Welcome {input_username}, let's analyze some text!")
elif input_username not in users_and_passwords:
    print("Unregistered user, terminating the program.")
    exit()
else:
    print("User or password incorrect, terminating the program.")
    exit()


number_of_texts = len(TEXTS)
min_number = 1                      # Hardcoded min. range, assuming the list is never empty.
                                    # Including check if the list is empty should be implemented,
                                    # but it was not part of the assignment.

print(f"We have {number_of_texts} texts to analyze")
print(line)
selected_text = input(f"Please select a number between {min_number} and {number_of_texts}:")

if not selected_text.isdigit():
    print("Invalid input, terminating the program.")
    exit()

choice = int(selected_text)

if choice < 1 or choice > number_of_texts:
    print("Invalid input, terminating the program.")
    exit()

selected_text = TEXTS[choice - 1]

sum_nums = 0                         #Storing counted values
numeric_count = 0
sum_words = 0
sum_words_UPPER = 0
sum_words_title = 0
sum_lowercase = 0

len_word_count = {}                 #List storing lengths of words


split_words = selected_text.split()
for text in split_words:
    sum_words += 1

for word in split_words:
    clean_word = word.strip(",.")                                            
    length = len(clean_word)                    
    len_word_count[length] = len_word_count.get(length, 0) + 1      #Counting the lengths of words and adding them into a list
    if clean_word.isnumeric():                  #Sum of all numeric characters
        sum_nums += int(word)
        numeric_count += 1
    if clean_word.istitle():
        sum_words_title += 1
    if clean_word.isupper():
        sum_words_UPPER += 1
    if clean_word.islower():
        sum_lowercase += 1
    


print(line)
print(f"There are {sum_words} words in the selected text.")
print(f"There are {sum_words_title} titlecase words.")
print(f"There are {sum_words_UPPER} uppercase words.")
print(f"There are {sum_lowercase} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers is {sum_nums}")
print(line)
print("LEN|     OCCURRENCES      |NR.")
print(line)
for length in sorted(len_word_count):
    count = len_word_count[length]
    print(f"{length:>2}| {"*" * count:<20}  |{count}")