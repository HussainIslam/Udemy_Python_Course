def sentence_maker(phrase):
  captalized = phrase.capitalize()
  key_words = ( 'how', 'why', 'when', 'what', 'where', 'which')
  if phrase.startswith(key_words):
    captalized = '{}?'.format(captalized)
  else:
    captalized = '{}.'.format(captalized)
  return captalized


def main():
  text_list = []
  while True:
    text = input("Say something: ")
    if text == '\end':
      break
    else:
      text_list.append(sentence_maker(text))
  for t in text_list:
    print(t, end=' ', flush= True)

if __name__=='__main__': main()