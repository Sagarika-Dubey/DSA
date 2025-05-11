from collections import Counter
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq=Counter(s)
        d_s= set(s)
        
        if len(d_s)==k:
            return 0
        
        fre_count= sorted(freq.values())
        dele=0
        distinct=len(fre_count)
        
        for i in fre_count:
            if distinct<=k:
                break
            dele+= i
            distinct-=1
            
        return dele
            
        