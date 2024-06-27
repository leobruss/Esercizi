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

def is_palindrome(head: Node) -> bool:
    if not head or not head.next:
        return True
    
    # Find the end of the first half and reverse the second half.
    def end_of_first_half(head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    # Find the end of the first half
    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(first_half_end.next)
    
    # Check whether or not there's a palindrome
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next
    
    # Restore the list (optional)
    first_half_end.next = reverse_list(second_half_start)
    
    return result




	
ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)
print(is_palindrome(ll1.head))

ll2 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll2.append(value)
print(is_palindrome(ll2.head))

ll3 = LinkedList()
ll3.append(1)
print(is_palindrome(ll3.head))

ll4 = LinkedList()
ll4.append(1)
ll4.append(1)
print(is_palindrome(ll4.head))

ll5 = LinkedList()
ll5.append(1)
ll5.append(2)
print(is_palindrome(ll5.head))