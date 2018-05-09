"""
Referencing 'Fundamentals of Physics' by David Halliday

1.1 is a section about units, and describes how we came ot the SI units, scientific notation, and the conversions
between larger and smaller quantities using different prefixes.

This program contains a dictionary of prefixes with their corresponding factors of conversion, a conversion function,
and a quiz on matching prefixes to their corresponding factors.

Author: Adam Gentz
"""

# dictionary containing the prefix to exponential values of each unit prefix
# from typing import Any, Union, KeysView
dict_prefixfactor = {'yocto' : -24, 'zepto' : -21, 'atto' : -18, 'femto' : -15,
                     'pico' : -12, 'nano' : -9, 'micro' : -6, 'milli' : -3, 'centi' : -2,
                     'deci' : -1, 'deka' : 1, 'hecto' : 2, 'kilo' : 3, 'mega' : 6,
                     'giga' : 9, 'tera' : 12, 'peta' : 15, 'exa' : 18, 'zetta' : 21,
                     'yotta' : 24}


# convert(unit) takes in a unit type (meter, liter, etc.) and attaches it to the chosen prefixes..
# then converting the unit based on user input
def convert(unit):
    # list containing the keys of the dictionary
    prefix_keys = list(dict_prefixfactor.keys())

    # print the instructions
    print('Use arrows (up/down) to navigate prefixes.\n------------------------')
    print('Initial value: ')
    text_option_cycle_menu(prefix_keys, 0)


# helper function to cycle text menu options in a dictionary
def text_option_cycle_menu(menu_options, starting_index):

    # menu_index is the tracker for which slot we are at in the key list
    menu_index = starting_index

    # while loop takes user input until they have decided on a choice
    while True:

        # print the menu option so the user knows which item they are on
        print('\r\033[1;1H' + menu_options[menu_index], end='')

        # take the users choice as input
        user_choice = input()

        # if the user presses enter, the menu index goes up
        if user_choice == '':
            # if the index is at the top, move it to the bottom
            if menu_index == len(menu_options) - 1:
                # index is the bottom of the list
                menu_index = 0
            else:
                # index is increased by one
                menu_index += 1
        # else break the loop, the user has chosen a prefix
        else:
            break


convert('meter')
