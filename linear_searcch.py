class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        for i in range (len(arr)):
            if arr[i]==k:
                return True

        return False
    
arr=[1,2,3,4,5,6]
k=6
sol= Solution()
print(sol.searchInSorted(arr,k))