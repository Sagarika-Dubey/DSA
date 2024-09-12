class Solution:
    def printGfg(self, n):
        # Code here
        if n<=0:
            return
        self.printGfg(n-1)
        print("GFG", end=" ")

n=int(input("Enter how many time u need to print GFG"))
solution=Solution()
solution.printGfg(n)