class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref,suf=[1],[1]
        for i,x in enumerate(nums[:-1]):
            pref.append(x*pref[i])
        for i,x in enumerate(reversed(nums[1:])):
            suf.append(x*suf[i])
        suf.reverse()
        out = [p*s for p,s in zip(pref,suf)]
        return out