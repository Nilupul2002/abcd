class Node:
    def _int_(self,data):
        self,deta=deta
        self,next=None

class LinkedList:
    #function to initializ head
   def _int_(self):
       self.head = None

    def listprint(self):
       printval=self.head
       while printval is not None:
           print (printval.data)
           printval=printval.next

    def _inset_at_Begining(self,newdata):
       newNode = Node(newdata)
       newNode.next = self.head
       self.head = newNode

l1 = LinkedList()
l1.head = Node("toyota")
l2 = Node("BMW")
l3 = Node("audi")
l4 = Node("lambogini")
l1.head.next = l2
l2.next = l3
l3.next = l4

# insert a new mode at the bigining
l1.insert_at_beginning("ford")

l1.listprint()
