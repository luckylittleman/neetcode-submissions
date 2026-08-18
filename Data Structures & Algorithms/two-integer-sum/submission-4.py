class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash={}

        for i,num in enumerate(nums):
            dif=target-num

            if dif in hash:
                return [hash[dif],i]
            else:
                hash[num]= i