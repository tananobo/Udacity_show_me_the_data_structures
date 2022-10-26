class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_output = []
    l1_node = llist_1.head
    l2_node = llist_2.head
    while l1_node:
        if l1_node.value not in union_output:
            union_output.append(l1_node.value)
        l1_node = l1_node.next
    while l2_node:
        if l2_node.value not in union_output:
            union_output.append(l2_node.value)
        l2_node = l2_node.next
    return union_output

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_output = []
    l1_node = llist_1.head
    l2_node = llist_2.head
    while l1_node:
        while l2_node:
            if l1_node.value == l2_node.value and l1_node.value not in intersection_output:
                intersection_output.append(l1_node.value)
            l2_node = l2_node.next
        l2_node = llist_2.head
        l1_node = l1_node.next
    return intersection_output


# Test case 1
# union_list should be [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11].
# intersection_list should be [4, 6, 21].

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
# union_list should be [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21].
# intersection_list should be [4, 6, 21].

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
# union_list should be [].
# intersection_list should be [].

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))