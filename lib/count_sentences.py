#!/usr/bin/env python3    
import re

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        '''Returns True if the value ends with a period, otherwise False.'''
        return self.value.endswith('.')

    def is_question(self):
        '''Returns True if the value ends with a question mark, otherwise False.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the value ends with an exclamation mark, otherwise False.'''
        return self.value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the value.'''
        if not self.value:
            return 0
       
        sentences = re.split(r'[.!?](?:\s+|$)', self.value.strip())
       
        return len([s for s in sentences if s])
