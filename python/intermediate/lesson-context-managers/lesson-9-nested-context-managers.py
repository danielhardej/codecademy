## lesson using context managers for opening, reading, writing multiple files
## part of Codecademy's intermediate Python course on nested context managers

from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File')
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File')
    open_card_file.close()

with card_files('card.txt', 'w') as card:
  with poem_files('poem.txt', 'r') as poem:
    print(card)
    print(poem)
    card.write(poem.read())
