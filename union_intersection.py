n=int(input("enter the no of elememts in array 1: "))
arr1=[]
for i in range(n):
    ele=int(input("Enter the element:"))
    arr1.append(ele)
m=int(input("enter the no of elememts in array 1: "))
arr2=[]
for i in range(m):
    ele=int(input("Enter the element:"))
    arr2.append(ele)
#sorting
arr1.sort()
arr2.sort()
set1=set(arr1)
set2=set(arr2)
arr1_u_arr2=set1.union(set2)
print("union of the arrays are:",arr1_u_arr2)
arr1_i_arr2=set1.intersection(set2)
print("intersection of the arrays are:",arr1_i_arr2)