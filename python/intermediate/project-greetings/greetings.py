from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, recipient):
  card_file = open(card_type, 'r')
  order = open(f"{sender_name}_generic.txt", 'w')

  try:
    order.write(f"Dear {recipient}, \n\n")
    order.write(card_file.read())
    order.write(f"\n\nSincerely, {sender_name} \n")
    yield order

  finally:
    card_file.close()
    order.close()

with generic("thankyou_card.txt", "Mwenda", "Amanda") as order:
  print('Card Generated! \n')

with open("Mwenda_generic.txt", "r") as first_order:
  print(first_order.read())

class Personalized:
  def __init__(self, sender, recipient):
    self.file = open(f"{sender}_personalized.txt", 'w')
    self.sender = sender
    self.recipient = recipient

  def __enter__(self):
    self.file.write(f"Dear {self.recipient}, \n\n")
    return self.file

  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write(f"\n \n Sincerely, \n {self.sender}")
    self.file.close()

with Personalized("John", "Michael") as personal_card:
  personal_card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")


with generic("happy_bday.txt", "Josiah", "Remy") as generic_card, Personalized("Josiah","Esther") as personal_card_2:
  personal_card_2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")

  
