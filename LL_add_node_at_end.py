'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        if head == None:
            return Node(x)
        if head.next is None:
            new_node = Node(x)
            return head
        temp = head
        while(temp.next):
            temp = temp.next
        new_node = Node(x)
        temp.next = new_node
        return head