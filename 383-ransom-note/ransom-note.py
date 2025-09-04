class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for a in ransomNote:
            if a in magazine :
                magazine=magazine.replace(a,"",1)
            else:
                return False
        return True            
        
        