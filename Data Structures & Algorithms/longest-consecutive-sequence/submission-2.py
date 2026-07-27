from functools import cache


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lcs to an index given prefix
        # base case: empty, then singleton
        # 1 + lcs upto that index with join cond if curr num is bigger
        # do naive way first with O(n^2) or worse
        # def longest_to(i)->list[int]:
        #     if i==0:return []
        #     return 1 + longest_to(i-1)
        # every elem either starts a LCS or is in one
        # naive soln: for each index, find all consec subseqs upto that index and pick longest
        if not nums: return 0
        out: dict[int, int] = {}  # idx: len
        S = set(nums)
        longest = 0
        for n in S:
            if n - 1 not in S:
                curr = 1
                while n + curr in S:
                    curr += 1
                longest = max(longest, curr)
        return longest

        def longest_from(i):
            if i == len(nums) - 1:
                return

        # if starts: 1 + longest after
        # otherwise in the middle,
        # if each idx starts a seq, then we can make seq by looking for n+1,n+2..
        def constr_seq(i):
            # tail
            if i == len(nums) - 1:
                return [nums[i]]
            else:
                try:
                    n = nums.index(nums[i] + 1)
                    return constr_seq(i - 1) + [nums[i] + 1]
                except ValueError:
                    return constr_seq(i - 1)

        out = {i: constr_seq(i) for i in range(len(nums))}  # idx : seq
        return max(out.values(), 0)