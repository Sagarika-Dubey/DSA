#User function Template for python3
class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        t1,t2=A,B
        def gcd(a,b):
            while b>0:
                r=a%b
                a=b
                b=r
            return a
        gcd_value= gcd(A,B)
        lcm= (t1*t2)//gcd_value
        return [lcm, gcd_value]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends