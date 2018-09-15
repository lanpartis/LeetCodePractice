class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        lheight=height[0]
        rheight=height[-1]
        size=0
        l=0
        r=len(height)-1
        while(l!=r):
            h = min(lheight,rheight)
            if height[l]<height[r]:
                n_size = lheight - height[l]
                if n_size<0:
                    n_size=0
                l+=1
                if height[l]>lheight:
                    lheight = height[l]
            else:
                n_size = rheight - height[r]
                if n_size<0:
                    n_size=0
                r-=1
                if height[r]>rheight:
                    rheight = height[r]
            size+=n_size
        return size
