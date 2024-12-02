class Solution:
    def myAtoi(self, s):
        # Code here
        sign=1
        res=0
        indx=0
        
        while indx<len(s) and s[indx]==' ':
            indx+=1
            
        if indx<len(s) and (s[indx]=="-" or s[indx]=='+'):
            if s[indx]=='-':
                sign=-1
            indx+=1
            
        while indx<len(s) and '0'<=s[indx]<='9':
            res=res*10+ (ord(s[indx])- ord('0'))
            if res> (2**31 -1):
                return sign*(2**31 -1) if sign==1 else -2**31
            indx+=1   
        return sign*res


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")