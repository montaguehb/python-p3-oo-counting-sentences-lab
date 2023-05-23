#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value =''):
    self.value = value

  def set_value(self):
    return self._value
  
  def get_value(self, value):
    try:
      if(type(value) == str):
        self._value = value
      else:
        raise TypeError
    except TypeError:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    return len(re.findall("[!?.]+(?=$|\s)", self.value))
  
  value = property(set_value, get_value)