class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	ans = [1]
    	while(ans[-1]<N):
    	    temp = ans[-1]*(len(ans)+1)
    	    if temp<=N:
        	    ans.append(temp)
        	else:
        	    break
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()