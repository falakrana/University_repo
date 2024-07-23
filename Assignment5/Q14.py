# Merge Intervals


class Solution:
    def merge(intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
