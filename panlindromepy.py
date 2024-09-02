class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        if(x<0):
            return False
        while(temp>0):
            a=temp%10
            rev=rev*10+a
            temp=temp//10
        if(rev==x):
            return True
        else:
            return False
        
x=int(input("Enter a number"))
solution=Solution()
print(solution.isPalindrome(x))