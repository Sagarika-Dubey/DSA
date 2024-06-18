# check for prime number
class Solution:
    def isPrime(self,x):
        count=0
        for i in range(1,x+1):
            if x%i==0:
                count+=1
        if count==2:
            print("Prime Number")
        else:
            print("Not a Prime number")
            
sol=Solution()
sol.isPrime(4)