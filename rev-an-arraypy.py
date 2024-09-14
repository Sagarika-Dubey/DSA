class Solution:
    def printNos(self,arr):
        return arr[::-1]

arr=[]
n=int(input("Enter how many elements you want to put?"))
for i in range(n):
    ele=int(input("enter Element"))
    arr.append(ele)   
solution=Solution()
print(solution.printNos(arr))