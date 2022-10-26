This code have two function:
1. union(linked_list1, linked_list2): it returns the union of linked_list1 and linked_list2.
2. intersection(linked_list1, linked_list2): it returns the intersection of linked_list1 and linked_list2 .

Time complexity of union function is O(n^2) because check all element in each linked_list and check if the element is not in output list every time.
Time complexity of intersection function is O(n^3) because check all combination between linked_list1 and linked_list2 and also check if the element is not in output list every time.
