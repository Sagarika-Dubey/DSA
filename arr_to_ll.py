class Solution:
    def constructLL(self, arr):
        # code here
        head = Node(arr[0])
        
        curr = head
        
        for i in range(1,len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
        return head