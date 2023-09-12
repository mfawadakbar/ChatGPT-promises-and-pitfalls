import random as rand


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def set_next(self, next):
        self.next = next

    # Recursive function to delete the linked list
    def delete_list(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            next_node = current_node.next
            del current_node
            self.head = None
            self.delete_list(next_node)


# Driver program to test above functions
llist = LinkedList()

rand_len = rand.randint(1, 100)
for i in range(rand_len):
    llist.push(rand.randint(1, 100))


print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
llist.deleteList()
print("\Deleted Linked List")
llist.printList()
