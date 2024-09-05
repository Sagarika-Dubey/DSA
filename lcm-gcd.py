import math
class Solution:
    def lcmAndGcd(self, A,B): 
        gcd=1
        for i in range(1,min(A,B)):
            if (A%i==0) and (B%i==0):
                gcd=i
        num=A*B
        lcm=math.trunc(math.trunc(num)/gcd)
        return lcm, gcd
x=int(input("Enter a Number1:"))
y=int(input("Enter a Number2:"))
solution=Solution()
print(solution.lcmAndGcd(x,y))