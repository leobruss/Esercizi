class DataStructureIntegrityError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        if not self.head:
            raise DataStructureIntegrityError("Cannot remove from an empty list.")
        
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if not current.next:
            raise DataStructureIntegrityError("Value not found in the list.")
        
        current.next = current.next.next

    def access(self, index):
        if not self.head:
            raise DataStructureIntegrityError("Cannot access an element in an empty list.")
        
        current = self.head
        current_index = 0

        while current and current_index < index:
            current = current.next
            current_index += 1

        if not current:
            raise DataStructureIntegrityError("Index out of range.")
        
        return current.value

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return

        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        if not self.head:
            return
        
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def is_ordered(self):
        if not self.head or not self.head.next:
            return True
        
        current = self.head
        while current.next:
            if current.value > current.next.value:
                return False
            current = current.next
        return True