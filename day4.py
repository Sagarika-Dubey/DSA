def rotate_arr(arr, r):
    n=len(arr)
    r%=n
    arr[:]=arr[r:]+arr[:r]
    return arr

arr=[1,2,3,4,5]
r=2
print(rotate_arr(arr,r))

