import string
alphabet = string.ascii_lowercase

def decrypt_cipher(encrypted_text, offset):
  # creat a list of encrypted words.
  encrypted_text_list = encrypted_text.split()

  # creat a list to hold decrypted words.
  output = []

  for word in encrypted_text_list:
    decrypted_word = []
    for char in word:
      if char == ' ':
        decrypted_word.append(' ')
      elif char == '!':
        decrypted_word.append("!")
      elif char == "?":
        decrypted_word.append("?")
      elif char == ".":
        decrypted_word.append(".")
      else:
        pos = alphabet.index(char) + offset
        if pos >= 25:
          pos -= 26
        decrypted_word.append(alphabet[pos])
    output.append(''.join(decrypted_word))

  # join each word in the sentence list back together by a space.
  output = ' '.join(output)
  print('Decryption Successful\n')
  print('Your decrypted sentence is:\n', output)
  return output

def encrypt_cipher(text, offset):
  # creat a list of words from input text.
  text_list = text.split()

  # creat a list to hold decrypted words.
  output = []

  for word in text_list:
    encrypted_word = []
    for char in word:
      if char == ' ':
        encrypted_word.append(' ')
      elif char == '!':
        encrypted_word.append("!")
      elif char == "?":
        encrypted_word.append("?")
      elif char == ".":
        encrypted_word.append(".")
      else:
        pos = alphabet.index(char) - offset
        if pos >= 25:
          pos -= 26
        encrypted_word.append(alphabet[pos])
    output.append(''.join(encrypted_word))

  # join each word in the sentence list back together by a space.
  output = ' '.join(output).lstrip(' ')
  print('Encryption Successful\n')
  print('Your encrypted sentence is:\n', output)
  return output


letter = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

decrypt_cipher(letter, 10)


letter_2 = "hello there this is a test sentence to encrypt"
letter_2_encrypt = encrypt_cipher(letter_2, 4)

letter_2_decrypt = decrypt_cipher(letter_2_encrypt, 4)


first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
decrypt_cipher(first_message, 10)

second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
decrypt_cipher(second_message, 14)


def decrypt_cipher_general(encrypted_text):
  alphabet = string.ascii_lowercase
  # creat a list of encrypted words.
  encrypted_text_list = encrypted_text.split()

  for offset in range(1, 26):
    # create a list to hold decrypted words.
    output = []
    for word in encrypted_text_list:
      decrypted_word = []
      for char in word:
        if char == ' ':
          decrypted_word.append(' ')
        elif char == '!':
          decrypted_word.append("!")
        elif char == "?":
          decrypted_word.append("?")
        elif char == ".":
          decrypted_word.append(".")
        elif char == "'":
          decrypted_word.append("'")
        else:
          pos = alphabet.index(char) + offset
          if pos >= 25:
            pos -= 26
          decrypted_word.append(alphabet[pos])
      output.append(''.join(decrypted_word))

    # join each word in the sentence list back together by a space.
    output = ' '.join(output)
    print(offset)
    print('Your decrypted sentence is:\n', output)


mystery_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
decrypt_cipher_general(mystery_message)
