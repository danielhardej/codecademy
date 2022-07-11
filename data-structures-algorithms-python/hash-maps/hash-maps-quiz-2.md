## Data Structures in Python: Hash Maps Quiz 2

#### Which of the following is not true about open addressing?

- [ ] It is a technique used to resolve collisions in a hash map.
- [ ] If it comes across an index with an existing key-value pair with a matching key, it replaces the value with the new value.
- [x] It will always place the new key-value pair into the hash map.
- [ ] It uses a variable to keep track of the current number of collisions, which is used to calculate a new array index that it will check next.

#### Fill in the code for the .assign() method:

    def assign(self, key, value):
      array_index = self.compressor(self.hash(key))
      current_array_value = self.array[array_index]

      if current_array_value is None:
        self.array[array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[array_index] = [key, value]
        return

      number_collisions = 1

      while(current_array_value[0] != key):
        new_hash_code = self.hash(key, number_collisions)
        new_array_index = self.compressor(new_hash_code)
        current_array_value = self.array[new_array_index]

        if current_array_value is None:
          self.array[new_array_index] = [key, value]
          return

        if current_array_value[0] == key:
          self.array[new_array_index] = [key, value]
          return

        number_collisions += 1

#### What is the purpose of the .compressor() method?

    def compressor(self, hash_code):
      return hash_code % self.array_size

- [ ] It compresses the size of the key-value pair so that it saves memory.
- [ ] It makes sure that the value of the new key-value pair can fit in the bounds of the array.
- [x] It ensures that the index is always within the bounds of the array.


#### Fill in the code for the following methods of the HashMap class:

    def hash(self, key, count_collisions=0):
      key_bytes = key.encode()
      hash_code = sum(key_bytes)
      return hash_code + count_collisions

    def compressor(self, hash_code):
      return hash_code % self.array_size

#### Fill in the code for the constructor method of the HashMap class which uses open addressing:

    class HashMap:
      def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

#### What will the following code do when there is a collision of keys?

    def hash(self, key):
      key_bytes = key.encode()
      hash_code = sum(key_bytes)
      return hash_code

    def compressor(self, hash_code):
      return hash_code % self.array_size

    def assign(self, key, value):
      array_index = self.compressor(self.hash(key))
      self.array[array_index] = [key, value]

- [ ] If there is a key collision, it will not replace the entry at the index.
- [x] If there is a key collision, it will replace the current entry at the index with the new key-value pair.
- [ ] If there is a key collision, it will keep the old key and replace the value at the index.

#### Fill in the code to finish the .retrieve() method:

    def retrieve(self, key):
      array_index = self.compressor(self.hash(key))
      possible_return_value = self.array[array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions = 1

      while (possible_return_value[0] != key):
        new_hash_code = self.hash(key, retrieval_collisions)
        retrieving_array_index = self.compressor(new_hash_code)
        possible_return_value = self.array[retrieving_array_index]

        if possible_return_value is None:
          return None

        if possible_return_value[0] == key:
          return possible_return_value[1]

        number_collisions += 1

      return
