class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        for i in range(len(b)):
            a.append(b[i])
            
        a.sort()
        unique_lst=list(dict.fromkeys(a))
        return unique_lst
    
a=[1,2,3,4]
b=[2,3,4,5,6]
sol=Solution()
print(sol.findUnion(a,b))
