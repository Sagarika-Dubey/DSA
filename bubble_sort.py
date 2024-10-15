class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n-1,0,-1):
            for j in range(0,i):
                if arr[j]>arr[j+1]:
                    temp=arr[j+1]
                    arr[j+1]=arr[j]
                    arr[j]=temp

arr=[]
n=int(input("Enter how many elements you want"))
for i in range(0,n):
    ele=int(input("Enter:"))
    arr.append(ele)
solution=Solution()
solution.bubbleSort(arr,n)
for i in range(n):
    print(arr[i], end=",")