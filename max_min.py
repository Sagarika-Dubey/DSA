n=int(input("enter how many numbes u want to enter in the array: "))
arr=[]
for i in range(0,n):
    ele=int(input("enter the term: "))
    arr.append(ele)
max_term=max(arr)
min_term=min(arr)
print("maximum term in the array is:", max_term)
print("manimum term in the array is:", min_term)