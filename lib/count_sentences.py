class MyString:
  def __init__(self,value=""):
    self.value=value
  def get_value(self):
    return self._value
  def set_value(self,newString):
    if isinstance(newString,str):
      self._value=newString
    else:
      print("The value must be a string.")
  value=property(get_value,set_value)
  def is_exclamation(self):
    return self._value.endswith("!")
  def is_sentence(self):
    return self._value.endswith(".")
  def is_question(self):
    return self._value.endswith("?")
  def count_sentences(self):
    value=self.value
    for punc in [".","!"]:
      value=value.replace(punc,"?")
    new_sentences = [s for s in value.split("?") if s]
    return len(new_sentences)