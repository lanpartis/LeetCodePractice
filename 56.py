class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        res = list()
        for i in intervals:
            if len(res)>0 and res[-1][1]>=i.start:
                if i.end>res[-1][1]:
                    res[-1][1] = i.end
            else:
                res.append([i.start,i.end])
        return res