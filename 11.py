class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head=0
        tail=len(height)-1
        maxi =0
        while head!=tail:
            size = min(height[head],height[tail])*(tail-head)
            if maxi < size:
                maxi = size
            if height[head]>height[tail]:
                tail-=1
            else:
                head+=1
        return maxi
