def ciphar(message_text,shift_space):
  original_msg=message_text
  tr_om=original_msg.lower();
  char_set="abcdefghijklmnopqrstuvwxyz"
  encrypted_text=""
  shifted=shift_space
  for char in tr_om:
    if char==' ':
      encrypted_text+=' '
    else:
      index=char_set.find(char)
      new_index=(index+shifted)%len(char_set)
      new_char=char_set[new_index]
      encrypted_text+=new_char
    
  print(encrypted_text)

ciphar("Welcome Nabila", 4)