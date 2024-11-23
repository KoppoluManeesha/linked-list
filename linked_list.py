class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class  Linkedlist(Node):
    def __init__(self):
        self.head=None
    def insertAtBegin(self,data):
        new_node=Node(data)
        new_node.next=new_node
        # if self.data is None:
        #     self.data=new_node
        #     return
        # else:
        #     new_node.next=self.data
        #     self.node=new_node
    def printLL(self):
      current_node = self.head
      while(current_node):
         print(current_node.data)
         current_node = current_node.next
# n=Node(2)
ls=Linkedlist()
ls.insertAtBegin(4)
ls.insertAtBegin(3)
ls.printLL()
