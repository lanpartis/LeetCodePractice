class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        return self.rotate_binary_search(0,len(nums)-1,nums,target)

    def binary_search(self, head,tail,nums,target):
        if head>tail:
            return -1
        if head==tail and target!=nums[head]:
            return -1
        mid = (head+tail)//2
        if nums[mid]<target:
            head = mid+1
        elif nums[mid]>target:
            tail = mid-1
        else:
            return mid
        return self.binary_search(head,tail,nums,target)
    
    def rotate_binary_search(self,head,tail,nums,target):
        if head>tail:
            return -1
        mid = (head+tail)//2
        if tail == head and nums[head]!=target:
            return -1
        if nums[mid]==target:
            return mid
        if nums[mid]>=nums[head]:
            if nums[mid]>target>=nums[head]:
                return self.binary_search(head,mid-1,nums,target)
            else:
                return self.rotate_binary_search(mid+1,tail,nums,target)
        else:
            if nums[mid]<target<=nums[tail]:
                return self.binary_search(mid+1,tail,nums,target)
            else:
                return self.rotate_binary_search(head,mid-1,nums,target)

