#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [item for item in num_list if item % 2 == 0]
    return even_numbers

def make_exclamation(sentence_list):
    # !using for loop
    # sentenceStrings = []

    # for item in sentence_list:
    #     sentenceStrings.append(f"{item}!")

    # return sentenceStrings

    # !using list comperehension
    sentence_exclamation = [f'{item}!' for item in sentence_list]
    return sentence_exclamation