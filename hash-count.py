class Solution:
    def hashCount(self, arr,n):
        visited=[False]*n
        for i in range(n):
            if(visited[i]==True):
                continue
            count=1
            for j in range(i+1,n):
                if(arr[i]==arr[j]):
                    visited[j]==True
                    count+=1
            print(arr[i],count)


n=int(input("Enter how many numbers you want in the array"))
arr=[]
for i in range(n):
    ele=int(input("Enter: "))
    arr.append(ele)

#q=int(input("enter how many numbers yu wanna find in the listed array: "))
soution=Solution()
soution.hashCount(arr,n)