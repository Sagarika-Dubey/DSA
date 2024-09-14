class Solution:
    def factorialNumbers(self, n):
    	#code here
        fact=1
        arr=[]
        for i in range(1,n):
            fact=fact*i
            if(fact<=n):
                arr.append(fact)
        return arr
    
n=int(input("Enter the number"))
solution=Solution()
print(solution.factorialNumbers(n))