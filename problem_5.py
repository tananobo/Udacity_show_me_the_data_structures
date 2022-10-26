import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        # hash_str = "We are going to encode this string of data!".encode('utf-8')

        # sha.update(hash_str)

        sha.update(self.data)

        return sha.hexdigest()

# TEST case 1
print("===TEST1===")
block_0 = Block(time.gmtime(), "Hello world!".encode('utf-8'), 0)
block_1 = Block(time.gmtime(), "I'm Noboru Tanase.".encode('utf-8'), block_0)
block_2 = Block(time.gmtime(), "How are you?".encode('utf-8'), block_1)
print(block_2.hash, block_2.previous_hash == block_1, block_2.previous_hash.previous_hash == block_0) # something_hashed, True, True

# TEST case 2: empty_data
print("===TEST2===")
block_0 = Block(time.gmtime(), "".encode('utf-8'), 0) # no error
print(block_0.hash)

# TEST case 3: same timestamp for hash
print("===TEST3===")
sametime = time.gmtime()
block_0 = Block(sametime, "Hello world!".encode('utf-8'), 0)
block_1 = Block(sametime, "Hello world!".encode('utf-8'), block_0)
block_2 = Block(sametime, "I'm Noboru Tanase.".encode('utf-8'), block_1)
print(block_0.hash, block_1.hash) # same hash
print(block_0.hash, block_2.hash) # different hash