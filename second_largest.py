class Solution:
    def second_larget(self, arr):
        if len(arr) < 2:
            return -1
        
        largest= float('-inf')
        second_largest=float('-inf')
        for i in arr:
            if i>largest:
                second_largest=largest
                largest=i
            elif largest>i>second_largest:
                second_largest=i
            else:
                continue

        if second_largest != float('-inf'):
            return second_largest
        else:
            return -1
            
arr=[]
for i in range(3):
    a= int(input("enter the number"))
    arr.append(a)

sol=Solution()
print(sol.second_larget(arr))
