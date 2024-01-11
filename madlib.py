welcome_message = """
*****************************************
**    Welcome to Rhett's Madlib App!   **

The game will prompt you to enter a word 
(one at a time) with specific requirements.
for example an Adjective, a None, a 
Number within a certain range, etc.
*****************************************
"""

print(welcome_message)

template_file_path = 'assets/dark_and_stormy_night_template.txt'

def read_template(template_file_path):
    try:
        with open(template_file_path, 'r') as file:
            template = file.read().strip()
            return template
    except FileNotFoundError as error:
        raise error


def parse_template(template):
    stripped_template = ""
    language_parts = []
    
    capturing = False
    current_part = ""
    
    # loop through template by character
    # if character is '{' set capturing to True
    # then next character concatenated onto string
    # when hit '}' capturing set to False
    # append to stripped version of string
    
    for char in template:
        if char == '{':
            capturing = True
            current_part = "" # initializes current_part when a new placeholder starts
        elif char == '}' and capturing:
            capturing = False
            language_parts.append(current_part)
            stripped_template += '{}'
        elif not capturing:
            stripped_template += char
        elif capturing:
            current_part += char # appends characters to current_part while capturing a placeholder
            
    return stripped_template, tuple(language_parts)  


def collect_user_words(language_parts):
    user_words = []
    
    for placeholder in language_parts:
        user_input = input(f"Enter a word for '{placeholder}': ")
        user_words.append(user_input)
    
    return tuple(user_words)

def merge(stripped_template, user_words):
    return stripped_template.format(*user_words)

def run_app():
    template = read_template(template_file_path)
    stripped_template, language_parts = parse_template(template)
    user_words = collect_user_words(language_parts)
    complete_madlib = merge(stripped_template, user_words)
    print(complete_madlib)

run_app()



# test_template = f"It was a {adjective1} and {adjective2} {noun_plural_1}."

# madlib_template = """
# Make Me A Video Game!

# I the {adjective1} and {adjective2} {first_name_1} have {verb_past_tense} {first_name_2}'s {adjective3} sister and plan to steal her {adjective4} {noun_plural_1}!

# What are a {animal_large} and backpacking {animal_small} to do? Before you can help {name_female}, you'll have to collect the {adjective5} {noun_plural_1} and {adjective5} {noun_plural_2} that open up the {number_1_to_50} worlds connected to A {first_name_3}'s Lair. There are {number_1} {noun_plural_3} and {number_2} {noun_plural_4} in the game, along with hundreds of other goodies for you to find.

# """

# print(f"{test_template}")
