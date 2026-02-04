from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter=Counter(ransomNote)
        mag_counter=Counter(magazine)

        for char,count in r_counter.items():
            if count>mag_counter[char]:
                return False
        return True

        
        