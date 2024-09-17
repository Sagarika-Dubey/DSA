class Solution:
    def hashCount(self, s,q):
        hash={}
        for i in range(len(s)):
            char=s[i]
            if char in hash:
                hash[char]+=1
            else:
                hash[char]=1
        for i in range (q):
            st=input("Enter the letter:  ")
            for char in st:
                if char in hash:
                    print(hash[char])
                else:
                    print("0")


s=input("Enter a string:  ")
q=int(input("enter how many numbers you wanna find in the string: "))
soution=Solution()
soution.hashCount(s,q)