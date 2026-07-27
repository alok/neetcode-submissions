import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # instead of hashmap, can find the other num `target-n` by binary search
        N = len(numbers)
        for i, n in enumerate(numbers):
            N = len(numbers)
            tgt = target - n
            idx = bisect.bisect_left(numbers, tgt, i, N)
            if i<idx<N and numbers[idx]==tgt:
                return [i+1,idx+1]
        # assume succ