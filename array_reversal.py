n=int(input("enter how many numbers u want to put in the array"))
arr=[]
for i in range(0,n):
    ele=int(input("enter the number"))
    arr.append(ele)

ptr=arr[::-1]
print(ptr)