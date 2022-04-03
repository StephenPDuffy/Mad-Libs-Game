# Stephen Duffy 03/24/2022
# This project is a version of the popular game "Mad Libs"
# Random words are written/excepted from the user and then added to pre-written stories read from text files

# Structure:
# Type "start" to randomly select a mad lib
# Reads from random mad lib file
# Prompts user answers (nouns, verbs, adjectives, etc)
# Asks if user would like to save mad lib to a text file (if yes, save as text file)

from random import randint
import Constant


def menu():
    user_input = str()

    # While the user input is not the string "Start", request user input
    while user_input.upper() != Constant.QUIT:
        # Prompts the user to type "Start" to begin the game
        user_input = input("Type \"Start\" to start the begin a game or \"Quit\" to end the program:\n")

        # Prompts user input again if input is incorrect
        if user_input.upper() != Constant.QUIT and user_input.upper() != Constant.START:
            print("Incorrect input. Please try again.")

        # Begins game
        if user_input.upper() == Constant.START:
            play_game()
    return


# Starts the Mad libs game
def play_game():
    selected_story = read_stories_file()

    # Separate the line of different required speech types into a list
    speech_types_string = selected_story[0]
    speech_types = speech_types_string.split(",")
    speech_types.pop()

    # Holds the user's funny responses
    user_input = []

    # Prompts user for input for each speech type (blanks) required by the story
    for line in speech_types:
        answer = input("Please enter a " + determine_speech_type(line) + ": ")
        user_input.append(answer)

    # Prints the completed story
    print("All done. Here is your story: \n")
    print_story(selected_story, user_input)
    print("\n ----------------------------------------------------------------------------------------")
    print("\nFunny stuff!")

    return


# Reads the Stories.txt file
def read_stories_file():
    # Creates a list of stories
    list_stories = []

    # Opens stories.txt
    f = open("Stories.txt", "r")

    # Defines a new line for reading the file line by line
    line = ""

    # Reads the file for the entirety of the collection of stories
    while line != Constant.END_OF_FILE:
        # Defines a new list for reading stories from the text file
        # Declares new list
        current_list = []

        # Reads the speech_types for each given story
        for x in f:
            # Reads the story for each line in a given story
            current_list.append(x)
            line = x

            if x.strip() == Constant.THE_END:
                current_list.pop(len(current_list) - 1)
                break

        # Adds the current story to the list of stories
        list_stories.append(current_list)

    f.close()

    # Remove the last item within the list of stories, the "END OF FILE" string
    list_length = len(list_stories)
    list_stories.pop(list_length - 1)

    # Pulls a random story from the list through using randomly generated numbers
    random_number = generate_random(len(list_stories))
    random_story = list_stories[random_number]

    return random_story


def generate_random(upper_bounds):
    # Generates a random number used to select a story at random
    # Number generated is between 0 and BLANK (the total range of stories pre-written) for the list's index
    random_number = randint(0, (upper_bounds - 1))

    return random_number


# Determines the which type of speech the answer is
def determine_speech_type(line):
    speech_type = "ERROR"

    if line == Constant.SINGULAR_NOUN:
        speech_type = Constant.SINGULAR_NOUN
    elif line == Constant.PLURAL_NOUN:
        speech_type = Constant.PLURAL_NOUN
    elif line == Constant.PERSON:
        speech_type = Constant.PERSON
    elif line == Constant.PLACE:
        speech_type = Constant.PLACE
    elif line == Constant.ITEM:
        speech_type = Constant.ITEM
    elif line == Constant.NUMBER:
        speech_type = Constant.NUMBER
    elif line == Constant.COLOR:
        speech_type = Constant.COLOR
    elif line == Constant.VERB_ENDING_IN_ING:
        speech_type = Constant.VERB_ENDING_IN_ING
    elif line == Constant.VERB_PAST_TENSE:
        speech_type = Constant.VERB_PAST_TENSE
    elif line == Constant.VERB_PRESENT_TENSE:
        speech_type = Constant.VERB_PRESENT_TENSE
    elif line == Constant.ADJECTIVE:
        speech_type = Constant.ADJECTIVE
    elif line == Constant.ADVERB:
        speech_type = Constant.ADVERB

    return speech_type


def print_story(story, answer):
    # Firstly, format finished story
    # Remove expected word types
    story.pop(0)

    # Combine full story as a single, formatted string
    finished_story = ""
    index_i = 0

    # Properly formats the string before joining it to the finished story
    for line in story:
        temp_string = line

        # If the line is the first in the story, indent the paragraph
        if index_i == 0:
            temp_string = "\t" + temp_string
        # If the first character in the line is not a period, comma, or quotation mark, add a space before the string
        if (temp_string[0] != "." and temp_string[0] != "," and temp_string[0] != "\"") and index_i != 0:
            temp_string = " " + temp_string
        # If the line is the constant THE_END, break (as the story is complete)
        if line == Constant.THE_END:
            break
        # If there are no more answers, add the remaining story alone
        if len(answer) == 0:
            finished_story += temp_string.rstrip()
        # If the character before the newline in the string is a quotation mark
        # ...then add the string and answer with no space between them
        elif temp_string[len(temp_string) - 2] == "\"":
            finished_story += temp_string.rstrip() + answer.pop(0).upper()
        # Join the string and answer together (with a space separating them) and add to the finished story
        else:
            finished_story += temp_string.rstrip() + " " + answer.pop(0).upper()

        index_i += 1

    # Secondly, print sentence by sentence
    index_j = 0
    while index_j < len(finished_story):
        if finished_story[index_j] == ".":
            print(finished_story[index_j])
        else:
            print(finished_story[index_j], end='')
        index_j += 1


# Runs program
menu()
