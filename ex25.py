# -*- coding: utf-8 -*-

def break_words(stuff):
        '''This funtion will break up words for us.'''
        words = stuff.split(' ')
        return words

def sort_words (words):
        '''Sorts the words.'''
        return sorted(words)

def print_first_word(words):
        '''Prints the first word after popping it off.'''
        word = list(words).pop(0)
        print (word)

def print_last_word(words):
        '''Prints the last word after popping it off.'''
        word = list(words).pop(-1)
        print (word)

def print_first_and_last(sentence):
        '''Prints the first and last words of the sentence.'''
        words = break_words(sentence)
        print_first_word(words)
        print_last_word(words)

def print_first_and_last_sorte(sentence):
        '''Sorts the words then prints the first and last one.'''
        words = sort_sentence(sentence)
        print_first_word(words)
        print_last_word(words)
