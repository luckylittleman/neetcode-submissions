class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      hash={}
      for num in nums:
        hash[num]=hash.get(num,0)+1
      
      buckets=[[]for _ in range(len(nums)+1)]
      for num,count in hash.items():
        buckets[count].append(num)

      res=[]
      
      for bucket in reversed(buckets):
        for element in bucket:
            res.append(element)
            if len(res)==k:
             return res

        



    
