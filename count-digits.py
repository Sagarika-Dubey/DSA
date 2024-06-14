#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
         N_str = str(N)
         count = 0
         
         # Iterate over each digit in the string
         for digit in N_str:
            # Convert the digit to an integer
            digit_int = int(digit)
            
            # Check if the digit evenly divides N
            if digit_int != 0 and N % digit_int == 0:
                count += 1
         
         return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends