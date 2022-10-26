
import sys
from collections import deque

def huffman_encoding(data):

    if len(data) == 0:
        print("Data should be at least 1 character long.")
        return None, None
    _, frequency_counted = count_frequency(data)
    # create Huffman Tree
    tree = HuffmanTree()
    while len(frequency_counted) > 1:
        node1 = minnode_pop(frequency_counted)
        node2 = minnode_pop(frequency_counted)
        node = tree.merge(node1,node2)
        frequency_counted.append(node)
    tree.head = frequency_counted[0]

    # encoding
    encoded_dict = {}
    d = deque()
    d.append(("",tree.head))
    while d:
        code, node = d.popleft()
        if node.char:
            encoded_dict[node.char] = code
            continue
        if node.leftchild:
            d.append((code + '0', node.leftchild))
        if node.rightchild:
            d.append((code + '1', node.rightchild))
    # print(encoded_dict)
    encoded_data = ""
    for d in data:
        encoded_data += encoded_dict[d]
    return encoded_data, tree

def count_frequency(data):

    dict_of_frequency = {}
    frequency_counted = []
    for c in data:
        if c in dict_of_frequency:
            dict_of_frequency[c] += 1
        else:
            dict_of_frequency[c] = 1
    for key, value in dict_of_frequency.items():
        frequency_counted.append(Node(value,key))
    return dict_of_frequency, frequency_counted

def minnode_pop(frequency_counted):

    minvalue = 10 ** 9
    index = 10 ** 9
    for i, item in enumerate(frequency_counted):
        if item.value < minvalue:
            minvalue = item.value
            index = i
    return frequency_counted.pop(index)

class Node:

    def __init__(self, value, char=None):
        self.leftchild = None
        self.rightchild = None
        self.value = value
        self.char = char

class HuffmanTree:

    def __init__(self):
        self.head = None

    def merge(self, node1, node2):
        node = Node(node1.value + node2.value)
        if node1.value <= node2.value:
            node.leftchild = node1
            node.rightchild = node2
        else:
            node.leftchild = node2
            node.rightchild = node1
        return node

def huffman_decoding(data,tree):

    decoded_data = ""
    pointer = 0
    node = tree.head
    while pointer < len(data):
        if node.char:
            decoded_data += node.char
            node = tree.head
            continue
        if data[pointer] == '0':
            node = node.leftchild
        else:
            node = node.rightchild
        pointer += 1
    if node.char:
        decoded_data += node.char
    return decoded_data

if __name__ == "__main__":
    codes = {}

    # TEST1: Udacity provided this.
    print("==========TEST1============")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    
    decoded_data = huffman_decoding(encoded_data, tree)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # it should be same as before decoding = 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))  # The bird is the word
    
    # TEST2: Udacity also provided this
    print("==========TEST2============")
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 1010101010101000100100111111111111111000000010101010101

    
    decoded_data = huffman_decoding(encoded_data, tree)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # it should be same as before decoding = 74
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # AAAAAAABBBCCCCCCCDDEEEEEE

    # TEST3: empty
    print("==========TEST3============")
    a_great_sentence = ""

    encoded_data, tree = huffman_encoding(a_great_sentence) # "Data should be at least 1 character long."
