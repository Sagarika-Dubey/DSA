n=int(input("enter how many items u want to enter: "))
arr=[]
neg_arr=[]
pos_arr=[]
maxi=0
for i in range(n):
    ele=int(input("enter the element: "))
    arr.append(ele)
for i in range(n):
    if arr[i]<0:
        neg_arr.append(arr[i])
    else:
        pos_arr.append(arr[i])

print("the negative elemets of the array given is",neg_arr)
print("the positive elemets of the array given is",pos_arr)
#sorting
arr.sort()
print(arr)
