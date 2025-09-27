class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
    def insert_at_beginning(self,data):
        new_node