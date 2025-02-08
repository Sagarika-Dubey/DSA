class Solution:
    def check(self, nums: list[int]) -> bool:
        sorted_arr=sorted(nums)
        for i in range(len(nums)):
            match=True
            for j in range(len(nums)):
                if nums[(i+j)%len(nums)] != sorted_arr[j]:
                    match= False
                    break
            if match ==True:
                return True


        return False

arr=[3,4,5,1,2]
sol=Solution()
print(sol.check(arr))