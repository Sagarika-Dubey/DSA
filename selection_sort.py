class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,n-1):
            min=i
            for j in range(i,n):
                if(arr[j]<arr[min]):
                    min=j
                    
            temp=arr[min]
            arr[min]=arr[i]
            arr[i]=temp

arr=[]
n=int(input("Enter how many elements you want"))
for i in range(0,n):
    ele=int(input("Enter:"))
    arr.append(ele)
solution=Solution()
solution.selectionSort(arr,n)
for i in range(n):
    print(arr[i], end=",")