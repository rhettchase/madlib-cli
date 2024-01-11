welcome_message = """
*****************************************
**    Welcome to Rhett's Madlib App!   **

The game will prompt you to enter a word 
(one at a time) with specific requirements.
for example an Adjective, a None, a 
Number within a certain range, etc.
*****************************************
"""

template_file_path = 'assets/make_me_a_video_game_template.txt'

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
    print(welcome_message)
    template = read_template(template_file_path)
    stripped_template, language_parts = parse_template(template)
    user_words = collect_user_words(language_parts)
    complete_madlib = merge(stripped_template, user_words)
    print(complete_madlib)

run_app()

