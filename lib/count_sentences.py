#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value =''):
    self.value = value

  def set_value(self, value):
    if(isinstance(value, str)):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    return len(re.findall("[!?.]+(?=$|\s)", self.value))
  
  value = property(lambda self: self._value,fset=set_value)