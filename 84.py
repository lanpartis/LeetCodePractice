class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack=[heights[0]]
        res = 0
        for i,h in enumerate(heights[1:]):
            if h>=stack[-1]:
                stack.append(h)
            else:
                width=1
                while len(stack)>0 and stack[-1]>h:
                    h_p=stack.pop()
                    res = h_p*width if h_p*width>res else res
                    width+=1
                for i in range(width):
                    stack.append(h)
        return res