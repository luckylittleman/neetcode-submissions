class Solution:
    def isValid(self, s: str) -> bool:
        paren=[]
        maping={"(":")", "[":"]", "{":"}"}
        
        for char in s:
            if char in maping:
                paren.append(char)

            else:
                if not paren or maping[paren[-1]]!=char:
                    return False
                paren.pop()
        
        return not paren