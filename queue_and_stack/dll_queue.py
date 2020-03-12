import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
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

    def enqueue(self, value):
        # add to the head of the queue
        self.storage.add_to_head(value)
        # increase count by 1
        self.size += 1

    def dequeue(self):
        # if the queue is not already empty, remove from the tail
        if self.size > 0:
            # decrease count by one
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size

# myQ = Queue()

# myQ.enqueue(4)
# myQ.enqueue(2)
# myQ.enqueue(1)
# myQ.enqueue(3)

# print(myQ)

# removeVal = myQ.dequeue()
# print(f'Removed: {removeVal}')
# print(myQ)

# print(f'Queue size now is at {myQ.size}')
