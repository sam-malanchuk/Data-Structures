"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return "empty"
        curr_node = self.head
        # "(3) <-> (5) <-> ..."
        output = ""
        output += f'({curr_node.value})'
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f' <-> ({curr_node.value})'
        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value)
        self.length += 1
        # adding to an empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update the head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value)
        self.length += 1
        # adding to an empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.prev = self.tail
            self.tail.next = new_node
            # update the head
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # find the node, remove, and move to head
        if node is self.head:
            return
        node_value = node.value
        # delete the node
        self.delete(node)
        self.add_to_head(node_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # find the node, remove, and move to tail
        if node is self.tail:
            return
        node_value = node.value
        # delete the node
        self.delete(node)
        self.add_to_tail(node_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # nodes pointing to the deleted item now point to the next/prev one 
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None and self.tail is None:
            return "empty list"
        # curr_node = self.head
        # max_value = curr_node.value
        # while curr_node.next is not None:
        #     if curr_node.value > max_value:
        #         max_value = curr_node.value
        #     curr_node = curr_node.next
        # return max_value
        curr_node = self.head
        max_node = curr_node
        while curr_node:
            if max_node.value < curr_node.value:
                max_node = curr_node
            curr_node = curr_node.next
        return max_node.value



# our_dll = DoublyLinkedList()
# our_dll.add_to_head(8)
# our_dll.add_to_head(3)
# our_dll.add_to_tail(13)
# our_dll.add_to_head(5)
# our_dll.add_to_tail(7)

# print(our_dll)
# print(f'our max value is: {our_dll.get_max()}')
# print("removing tail", our_dll.tail.value)
# our_dll.remove_from_tail()
# print(our_dll)
# print("deleting", our_dll.head.next.next.value)
# our_dll.delete(our_dll.head.next.next)
# print(our_dll)

# print("The max is: ", our_dll.get_max())