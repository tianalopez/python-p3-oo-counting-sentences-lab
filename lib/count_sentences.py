#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if "." in self.value else False

  def is_question(self):
    return True if "?" in self.value else False

  def is_exclamation(self):
    return True if "!" in self.value else False

  def count_sentences(self):
    sentence_array = self.value.replace("!", ".").replace("?", ".").split(".")
    return len([sentence for sentence in sentence_array if sentence])
