# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): Nick Tang, Yuto Yoshimori
# ----------------------------------------------------------------------
"""
This program is a chatbot that chats with a user.

takes in a user's name and repeatedly gives replies based on user input.
This chatbot follows 12 rules, listed in the chat_with() function below.
"""
import random
import string

# Constants
pronoun_to_replacement = {
    'i': 'you',
    'am': 'are',
    'my': 'your',
    'your': 'my',
    'me': 'you',
    'you': 'me'
}
topics = {'family', 'friend', 'friends', 'mom', 'dad', 'brother', 'sister',
          'girlfriend', 'boyfriend', 'children', 'son', 'daughter',
          'child', 'wife', 'husband', 'home', 'cat', 'pet'}
answer_5 = [', why do you ask?', ', how would an answer to that help you?']
answer_6 = ['What do you think', 'Why is that important']
answer_10 = ['I have no clue.', 'Maybe.']
answer_12 = ["That's interesting.", "That's nice!", "Can you elaborate on "
                                                    "that?"]


# Helper functions
def change_person(*args):
    """
    This function takes an input of a sentence in the form of a list of
    words, changes/reverses the person of the sentence, then returns
    that sentence as a string.

    :param args: (string) one or more strings that form a sentence
    :return: (string) a sentence where the person are reversed
    """
    changed_sentence = [pronoun_to_replacement[word] if word in
                                                        pronoun_to_replacement else word
                        for word in strip_list_punc(*args)]
    return ' '.join(changed_sentence)


def special(word_list):
    """
    This function determines intersection between word_list and
    special_topics. If there are multiple items within the
    intersection, one random item out of the intersection will be
    returned.

    :param word_list: (list) words that make up a sentence
    :returns: (string/None) word that intersects word_list and topics,
                or None if no intersection
    """
    inter = set(strip_list_punc(word_list)) & topics
    if len(inter) > 0:
        return random.choice(list(inter))
    return None


def strip_list_punc(word_list):
    """
    This function takes a list of strings and strips them of their
    punctuation.

    :param word_list: (list) words that make up a sentence
    :return: (list) word_list with words stripped of punctuation
    """
    return [word.strip(string.punctuation) for word in word_list]


def is_question(word_list):
    """
    This function takes a list of strings and returns the end
    punctuation symbol.

    :param word_list: (list) words that make up a sentence
    :return: (string) end punctuation symbol if exists
    """
    if (word_list[-1][-1]) == '?':
        return True
    return False


# Core function
def chat_with(name):
    """
    This function prompts the user to enter a message, and
    prints/returns a message based on the input.

    :param name: string
    :return: Boolean
    """
    request = input('Talk to me please > ')
    lowered_request = request.lower().split()

    match lowered_request:
        # Rule 1: bye(.) => (exit case)
        case ['bye' | 'bye.']:
            print(f"Bye {name}.\nHave a great day!")
            return True

        # Rule 2: special topic
        case lowered_request if res := special(lowered_request):
            print(f'Tell me more about your {res}.')

        # Rule 3: (do/can/will) you ___ ?
        case [('do' | 'can' | 'will') as verb, 'you', *rest] if \
             is_question(rest):
            print(f'No {name}, I {verb} not {change_person(rest)}.')

        # Rule 4: why ___ ?
        case ['why', *rest] if is_question(rest):
            print('Why not?')

        # Rule 5: how ___ ?
        case ['how', *rest] if is_question(rest):
            print(f'{name}{random.choice(answer_5)}')

        # Rule 6: what ___ ?
        case ['what', *rest] if is_question(rest):
            print(f'{random.choice(answer_6)} {name}?')

        # Rule 7: i (need/think/have/want)
        case ['i', ('need' | 'think' | 'have' | 'want') as verb, *rest]:
            print(f'Why do you {verb} {change_person(rest)}?')

        # Rule 8: i ___ (last word is not too)
        case ['i', *end] if end[-1] != 'too':
            print(f'I {" ".join(end)} too.')

        # Rule 9: (verb list word) ___
        case [('tell' | 'give' | 'say') as verb, *rest]:
            print(f'You {verb} {" ".join(strip_list_punc(rest))}.')

        # Rule 10: ___ ?
        case lowered_request if is_question(lowered_request):
            print(random.choice(answer_10))

        # Rule 11: input contains because
        case lowered_request if 'because' in lowered_request:
            print('Is that the real reason?')

        # 12: everything else
        case _:
            print(random.choice(answer_12))

    return False


def main():
    # 1.Prompt the user for their name
    username = input("Hello. What is your name please? ")

    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.
    #   This is implemented in chat_with().
    done = False
    while not done:
        done = chat_with(username)


if __name__ == '__main__':
    main()
