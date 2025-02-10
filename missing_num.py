class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            flag=0
            for j in range(len(nums)):
                if nums[j]==i:
                    flag=1
                    break
            if flag==0:
                return i

        return (len(nums))