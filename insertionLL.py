# Node class
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def InsertAtHead(head, data):
    dummy=ListNode(data)
    dummy.next=head
    return dummy

def InsertAtEnd(head,data):
    dummy=ListNode(data)
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=dummy
    return head 

def InsertAtPos(head, data,pos):
    dummy=ListNode(data)
    temp=head
    counter=1
    while temp.next:
        if counter ==(pos-1):
            break
        temp=temp.next
        counter+=1
    dummy.next=temp.next
    temp.next=dummy
    
    return head




def printList(head):
    temp=head
    while temp:
        print(temp.val, end="->")
        temp=temp.next
    print("None")

## Main code
def convertArray2LL(arr):
    if not arr:
        return None
    head=ListNode(arr[0])
    temp=head
    for i in arr[1:]:
        temp.next=ListNode(i)
        temp=temp.next
    return head

arr=[12,8,5,3,1,7,10]
head=convertArray2LL(arr)
printList(head)
#print("\n")
printList(InsertAtHead(head, 100))
printList(InsertAtEnd(head, 20))
printList(InsertAtPos(head, 50, 3))