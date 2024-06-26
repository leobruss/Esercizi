from custom_exception import LinkedList, DataStructureIntegrityError

# Initialize linked list
ll = LinkedList()

# Append elements to the linked list
ll.append(3)
ll.append(5)
ll.append(7)
ll.print_list()

# Access elements
try:
    print("Element at index 1:", ll.access(1))
except DataStructureIntegrityError as e:
    print(f"DataStructureIntegrityError: {e}")

# Remove elements
try:
    ll.remove(5)
    ll.print_list()
except DataStructureIntegrityError as e:
    print(f"DataStructureIntegrityError: {e}")

# Check if list is ordered
print("Is the list ordered?:", ll.is_ordered())

# Reverse the list
ll.reverse()
ll.print_list()

# Try accessing an out-of-range index
try:
    print("Element at index 10:", ll.access(10))
except DataStructureIntegrityError as e:
    print(f"DataStructureIntegrityError: {e}")

# Try removing from an empty list
try:
    ll.remove(10)  # Removing an element not in the list to empty it
    ll.remove(3)
    ll.remove(7)
    ll.remove(1)  # This should raise an error
except DataStructureIntegrityError as e:
    print(f"DataStructureIntegrityError: {e}")

# Try accessing an element from an empty list
try:
    print("Element at index 0:", ll.access(0))
except DataStructureIntegrityError as e:
    print(f"DataStructureIntegrityError: {e}")