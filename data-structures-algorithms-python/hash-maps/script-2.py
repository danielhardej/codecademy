# In our previous implementation, all keys that resolve to the same index are treated
# as if they are the same key.
#
# Our first step in implementing a collision strategy is updating our .assign() and
# .retrieve() methods to set the value with the key and check the key before
# retrieving a value.
#
# To do this, we’re going to implement an open addressing system so our hash map
# can resolve collisions. In open addressing systems, we check the array at the
# address given by our hashing function.


class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)

    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
    elif current_array_value is not None:
      if current_array_value[0] == key:
        self.array[array_index] = [key, value]

    # if current_array_value currently holds different key
    number_collisions = 1
    while current_array_value[0] != key:
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return
      elif current_array_value == key:
        self.array[new_array_index] = [key, value]
        return
      elif current_array_value != key:
        if current_array_value is not None:
          number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    retrieval_collisions = 1
    while possible_return_value[0] != key:
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]
      if possible_return_value is None:
        return None
      if possible_return_value[0] == key:
        return possible_return_value[1]
      retrieval_collisions += 1
    return


# Test out the hash map!

hash_map = HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))
