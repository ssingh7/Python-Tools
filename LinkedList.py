class Node:
    def __init__(self,contents=None,next=None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)


def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()
    
def addNode(head,node):
    node.next = head
    head = node
    return node
    #print_list(head)

def deleteNode(node,content):
    while node:       
        if node.getContents()==content:
            print(node.getContents())
            print(node.next)
            node.next
            break
        else:
            node = node.next


def testList():
    head= Node('one')
    node2 = Node('two')
    node3 = Node('three')
    head.next = node2
    node2.next = node3
    
    node4 = Node('four')
    head = addNode(head=head,node=node4)
    node5 = Node('5')
    head = addNode(head=head,node=node5)
    #print_list(head)
    deleteNode(head,'three')


    
testList()
