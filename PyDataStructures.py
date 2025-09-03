# --- Data Structure: Linked List ---
# A simple Node class to represent an element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A simple Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to print the list (for testing)
    def print_list(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements))

    # Helper method to convert the linked list to a Python list
    # This is useful for passing data to the sorting algorithm.
    def to_list(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

# --- Algorithm: Bubble Sort ---
# A function to perform Bubble Sort on a list and track the steps.
def bubble_sort_visualize(arr):
    n = len(arr)
    steps = []  # This list will store the state of the array at each step for visualization
    
    # Store the initial state
    steps.append({'array': list(arr), 'pointers': [], 'message': 'Initial array'})

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Store the state before the comparison
            steps.append({
                'array': list(arr),
                'pointers': [j, j + 1],
                'message': f'Comparing {arr[j]} and {arr[j+1]}'
            })
            
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
                # Store the state after the swap
                steps.append({
                    'array': list(arr),
                    'pointers': [j, j + 1],
                    'message': f'Swapping {arr[j+1]} and {arr[j]}'
                })
        
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break
            
    steps.append({'array': list(arr), 'pointers': [], 'message': 'Array is sorted!'})
    return steps

# --- Example Usage ---
# 1. Using the Linked List
print("--- Linked List Example ---")
my_linked_list = LinkedList()
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.print_list()  # Output: 10 -> 20 -> 30

# 2. Using the Bubble Sort Algorithm
print("\n--- Bubble Sort Example ---")
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original Array: {data}")

# Run the sort and get all the steps
sort_steps = bubble_sort_visualize(data)

# Print the steps to see the output. This is what you would send to your web frontend.
for step in sort_steps:
    print(f"Step: {step['message']}")
    print(f"  Array: {step['array']}")
    # In the frontend, you would use 'pointers' to highlight the elements being compared/swapped.
    print(f"  Pointers: {step['pointers']}\n")