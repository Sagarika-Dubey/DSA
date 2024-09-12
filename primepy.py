class Solution:
	def minJumps(self, arr):
		count=0
		for j in range(arr):
			if arr%j==0:
				count+=1
		if count==2:
			print("Prime Number")
		else:
			print("Not a prime Number")
			
arr=int(input("Enter a Number"))
solution=Solution()
solution.minJumps(arr)