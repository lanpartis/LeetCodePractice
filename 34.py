class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        return [self.binary_search_head(0,len(nums)-1,nums,target),self.binary_search_tail(0,len(nums)-1,nums,target)]

        
    def binary_search_head(self, head,tail,nums,target):
        if (head==tail and nums[head]!=target) or head>tail:
            return -1
        mid = (head+tail)//2
        if (mid==head or nums[mid-1]!=target)and nums[mid]==target:
            return mid
        if nums[mid]>=target:
            return self.binary_search_head(head,mid-1,nums,target)
        else:
            return self.binary_search_head(mid+1,tail,nums,target)
    
    def binary_search_tail(self, head, tail, nums, target):
        if (head==tail and nums[head]!=target) or head>tail:
            return -1
        mid = (head+tail)//2
        if (mid==tail or nums[mid+1]!=target)and nums[mid]==target:
            return mid
        if nums[mid]<=target:
            return self.binary_search_tail(mid+1,tail,nums,target)
        else:
            return self.binary_search_tail(head,mid-1,nums,target)

