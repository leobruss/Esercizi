class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def get_node(self, pos):
        current = self.head
        index = 0
        while current and index < pos:
            current = current.next
            index += 1
        return current

def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False



ll1 = LinkedList()
for i in range(5):
    ll1.append(i)
node1 = ll1.get_node(1)  # Node with value 1
node4 = ll1.get_node(4)  # Node with value 4
node4.next = node1  # Creating a cycle

print(has_cycle(ll1.head))