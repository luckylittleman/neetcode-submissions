class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}

        for s in strs:
            kye=''.join(sorted(s))
            if kye not in hash:
                hash[kye]=hash.get(kye,[])
            hash[kye].append(s)

        return list(hash.values())


            
            


        

        