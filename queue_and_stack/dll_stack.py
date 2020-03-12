import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # it has the needed essentials of a list that has a beggining and end
        self.storage = DoublyLinkedList()

    def __str__(self):
        if self.storage.head is None and self.storage.tail is None:
            return "empty"
        curr_node = self.storage.head
        output = ""
        output += f'({curr_node.value})'
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f' <-> ({curr_node.value})'
        return output

    def push(self, value):
        # add to head
        self.storage.add_to_head(value)
        # increase count by 1
        self.size += 1

    def pop(self):
        # if the stack has at least one item, remove it
        if self.size > 0:
            # decrease count by one
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

# myStack = Stack()

# print("Adding 4")
# myStack.push(4)
# print(myStack)
# print("Adding 2")
# myStack.push(2)
# print(myStack)
# print("Adding 1")
# myStack.push(1)
# print(myStack)
# print("Adding 3")
# myStack.push(3)
# print(myStack)

# removeVal = myStack.pop()
# print(f'Popped from top: {removeVal}')
# print(myStack)

# print(f'Stack size now is at {myStack.len()}')
