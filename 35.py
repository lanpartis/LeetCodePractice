class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        return self.binary_search(0,len(nums)-1,nums,target)
    
    def binary_search(self, head, tail, nums, target):
        if tail<head:
            return head
        if head==tail:
            return head if nums[head]>=target else head+1
        mid = (head+tail)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            return self.binary_search(head,mid-1,nums,target)
        else:
            return self.binary_search(mid+1,tail,nums,target)

