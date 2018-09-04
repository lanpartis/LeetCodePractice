class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        half_len = (len(nums1)+len(nums2)+1)//2
        la,lb = (nums1,nums2) if len(nums2)> len(nums1) else (nums2,nums1)
        h,t = [0,len(la)]
        while h<= t:
            ia = (h+t)//2
            ib = half_len - ia
            if ia< len(la) and la[ia]<lb[ib-1]:
                h = ia+1
            elif ia>0 and la[ia-1]>lb[ib]:
                t = ia-1
            else:
                if ia==0: max_left = lb[ib-1]
                elif ib ==0: max_left = la[ia-1]
                else: max_left = max(la[ia-1],lb[ib-1])

                if (len(nums1)+len(nums2))%2 ==1:
                    return max_left

                if ia ==len(la): min_right = lb[ib]
                elif ib ==len(lb): min_right = la[ia]
                else :min_right = min(lb[ib],la[ia])

                return (max_left+min_right)/2
