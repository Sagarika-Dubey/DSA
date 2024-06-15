import math

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        while x!=0:
            if rev>((2**31)-1)/10 or  rev<(-2**31)/10:
                return 0
            elif x>0:
                a=x%10
                rev=rev*10+a
                x=math.trunc(x/10)
            else:
                a=x%-10
                rev=rev*10+a
                x=math.trunc(x/10)
        return rev    

sol=Solution()
a=sol.reverse(-120)
print(a)