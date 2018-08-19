class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable=dict()
        result=list()
        for i in range(len(nums)):
            hashtable[nums[i]]=i
        for i in range(len(nums)):
            if hashtable.get(target-nums[i]):
                if i<hashtable[target-nums[i]]:
                    result.extend([i,hashtable[target-nums[i]]])
        return result
