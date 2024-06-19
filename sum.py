class Solution:
    def sumOfSeries(self,n):
        #code here
        if n==0:
            return 0
        else:
            return (n * (n + 1) // 2) ** 2
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends