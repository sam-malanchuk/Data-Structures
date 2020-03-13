from doubly_linked_list import DoublyLinkedList

# return the middle node of the DLL, if there are two nodes, return the left one
# no empty list, length >= 1
# we don't know the length
# in a single pass
# not sorted
# 1 - 2 - 3 : 2
# 1 - 2 - 3 - 4 : 2
def find_middle(dll):
    head = dll.head
    tail = dll.tail

    while head != tail and head.next != tail:
        head = head.next
        tail = tail.prev

    return head.value

odd_nums = DoublyLinkedList()
[odd_nums.add_to_head(i) for i in [5, 3, 4, 10, 7]]
print(find_middle(odd_nums))

even_nums = DoublyLinkedList()
[even_nums.add_to_tail(i) for i in [5, 3, 4, '10', 7, 8]]
print(find_middle(even_nums))

list_1 = DoublyLinkedList()
list_1.add_to_head(10)
print(find_middle(list_1))

list_2 = DoublyLinkedList()
list_2.add_to_head(11)
list_2.add_to_head(13)
print(find_middle(list_2))
