class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for num in nums:
            xor^=num
        return xor
                    


nums=[2,2,1]
sol=Solution()
print(sol.singleNumber(nums))

#//
#brute force approach

class Solution1:
    def singleocc(self, nums):
        frequency={}
        for num in nums:
            if num not in frequency:
                frequency[num]=1
            else:
                frequency[num]+=1
        for key in frequency:
            if frequency[key]==1:
                return key
            
sol1=Solution1()
print(sol1.singleocc(nums))