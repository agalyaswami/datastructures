class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
    def listprint(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"==>",end=' ')
            temp=temp.next
    def atbeginning(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
#create an object        
list=slinkedlist()
#given a data
list.head=node("mon")
e2=node("tue")
e3=node("wed")
#connect the node
list.head.next=e2
e2.next=e3
#beggining data insert
list.atbeginning("sun")
list.listprint()
