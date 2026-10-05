class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for num in nums :
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
                
        result = sorted(count, key=count.get, reverse=True )

        return result[:k]

        