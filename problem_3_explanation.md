For this code, data is encoded into Huffman style. and huffman format is decoded into original sentence.

In the creating Huffman tree of the encoding part, time compelxity takes O(n^2) because all nodes are checked when code look for the node with minimum value. 
In the decoding part, time complexity takes O(nlogn) because every binary code will serch from Huffman tree (binary tree).
