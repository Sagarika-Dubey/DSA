class Solution:
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(0,n):
            j=i
            while(j>0 and alist[j-1]>alist[j]):
                temp=alist[j-1]
                alist[j-1]=alist[j]
                alist[j]=temp
                
                j-=1

arr=[]
n=int(input("Enter how many elements you want"))
for i in range(0,n):
    ele=int(input("Enter:"))
    arr.append(ele)
solution=Solution()
solution.insertionSort(arr,n)
for i in range(n):
    print(arr[i], end=",")