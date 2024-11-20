#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        large= sec_large=float('-inf')
        
        for i in arr:
            if i>large:
                sec_large=large
                large=i
            elif large>i> sec_large:
                sec_large=i
            else:
                continue
            
        return sec_large if sec_large!= float('-inf') else -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends