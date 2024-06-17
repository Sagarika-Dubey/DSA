class Solution:
    def armstrong(self, x):
        self.x=x
        temp=x
        temp1=x
        cube=0
        c=0
        while temp1>0:
            temp1//=10
            c=c+1
        while temp>0:
            a=temp%10
            cube=a**c+cube
            temp//=10
        if (x== cube):
            print("the number is an armstrong")
        else:
            print("The given number is not a armstrong")


sol =Solution()
sol.armstrong(1634)