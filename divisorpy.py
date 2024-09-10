class Solution:
    def sumOfDivisors(self, N):
        div=0
        for i in range(1,N+1):
            if(N%i==0):
                div=div+i
        return div

t = int(input("Enter a number"))
ob = Solution()
ans = ob.sumOfDivisors(t)
print(ans)
