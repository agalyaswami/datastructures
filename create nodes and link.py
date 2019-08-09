class node:
    def __init__(self,data):
        self.data=data
        self.address=None
n1=node(100)
n2=node(200)
n3=node(300)
n4=node(400)
n5=node(500)
n1.address=n2
n2.address=n3
n3.address=n4
n4.address=n5
temp=n1
while temp!=None:
    print(temp.data,"==>",end=' ')
    temp=temp.address
#print(n1.data,n2.data,n3.data,n4.data,n5.data)
