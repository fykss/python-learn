# Implementation of Linked List. https://www.geeksforgeeks.org/linked-list-set-1-introduction/
# https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/
# TODO: impl linked list


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def printList(self):
        pass

    def len(self):
        return self.size

    def add(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head


if __name__ == "__main__":
    l_list = LinkedList()

    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    l_list.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node
