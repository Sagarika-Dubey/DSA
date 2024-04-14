arr=[1,2,3,4,5]
arr[:]=arr[5-1:]+arr[:5-1]
print(arr)
