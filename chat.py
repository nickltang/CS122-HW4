# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): Nick Tang, Yuto
# ----------------------------------------------------------------------
"""
Enter your docstring with a one-line overview here

and a more detailed description here.
"""
import random
import string

# Enter your constant assignments below
pronoun_to_replacement = {
    'i': 'you',
    'me': 'you',
    'your': 'my',
    'my': 'your',
    'you': 'me'
}
topics = ['family', 'friend', 'friends', 'mom', 'dad',
                  'brother', 'sister', 'girlfriend', 'boyfriend',
                  'children', 'son', 'daughter', 'child', 'wife',
                  'husband', 'home', 'cat', 'pet']
answer_5 = []
answer_6 = []
answer_10 = ['I have no clue.', 'Maybe.']
answer_12 = ["That's interesting.", "That's nice!", "Can you elaborate on "
                                                    "that?"]


def change_person(*args):
    """
    This function changes the subject noun for a sentence that is split
    up by word.

    :param args: string
    :return: string
    """
    print()
    return ''


def special(list1, list2):
    """
    This function finds the intersection between two lists and returns
    that intersection as a list.

    :param list1: list
    :param list2: list
    :return: list
    """
    list(set(list1) & set(list2))


def strip_list_punc(word_list):
    return [word.strip(string.punctuation) for word in word_list]



def chat_with(name):
    """
    This function prompts the user to enter a message, and
    prints/returns a message based on the input.

    :param name: string
    :return: Boolean
    """
    request = input('Talk to me please > ')
    lowered_request = request.lower().split()
    print(len(set(lowered_request) & set(topics)))
    match lowered_request:
        # 1: bye(.) => (exit case)
        case ['bye' | 'bye.']:
            print(f"Bye {name}.\nHave a great day!")
            return True
        # 2: special topic
        case lowered_request if intersect(lowered_request, topics)) \
            > 0:
            print(f'Tell me more about '
                  f'{random.choice(intersect(lowered_request, topics))}.')

        # 3: (do/can/will) you ___ ?
        case [('do' | 'can' | 'will') as verb, 'you', *rest]:
            print(f'No {name}, I {verb} not {change_person(rest)}')
        # 4: why ___ ?
        case ['why', *rest]:
            print('Why not?')
        # 5: how ___ ?
        case ['how', *rest]:
            print('f')
        # 6: what ___ ?
        case ['what', *rest]:
            print()
        # 7: i (need/think/have/want)
        case ['i', ('need' | 'think' | 'have' | 'want') as verb, *rest]:
            print(f'Why do you {verb} {change_person(rest)}')
        # 8: i ___ (last word is not too)
        case ['i', *middle] if middle[-1] != 'too':
            print(f'I {middle} too.')
        # 9: (verb list word) ___
        case [('tell' | 'give' | 'say') as verb, *rest]:
            print(f'You {verb} {rest.join(" ")}.')
        # 10: ___ ?
        case [*sentence, last] if last[-1] == '?':
            print(random.choice(answer_10))
        # 11: input contains because
        case [lowered_request] if 'because' in lowered_request:
            print('Is that the real reason?')
        # 12: everything else
        case _:
            print(random.choice(answer_12))

    return False


def main():
    # Enter your code following the outline below and take out the
    # pass statement.
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
