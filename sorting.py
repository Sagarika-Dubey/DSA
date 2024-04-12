n=int(input("enter the no of elememts in array 1: "))
arr1=[]
for i in range(n):
    ele=int(input("Enter the element:"))
    arr1.append(ele)
arr1.sort()
print("sorted array is: ",arr1)