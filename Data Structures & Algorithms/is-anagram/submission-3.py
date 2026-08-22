class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hash_s={}
            hash_t={}

            for char in s:
                hash_s[char]=hash_s.get(char,0) + 1
            
            for char in t:
                hash_t[char]=hash_t.get(char,0) + 1
        
        if hash_s == hash_t:
            return True
        else:
            return False

     