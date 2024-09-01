class Solution:
    def reverse(self, x: int) -> int:
        temp= abs(x)
        rev=0
        while (temp!=0):
            if rev>((2**31)-1)/10 or  rev<(-2**31)/10:
                return 0
            a= temp%10
            rev=rev*10+a
            temp=temp//10
        if x<0:
            rev=rev*(-1)
        return rev

n=int(input("Enter the number u want to reverse"))   
solution=Solution()
print(solution.reverse(n))

