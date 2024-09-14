class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower=s.lower()
        clean_text="".join(char for char in s_lower if char.isalnum())
        rev_text=clean_text[::-1]

        if rev_text==clean_text:
            return True
        else:
            return False
    
s=input("Enter your string")
solution=Solution()
print(solution.isPalindrome(s))