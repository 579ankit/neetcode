class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        off=0
        cm=1
        n=len(nums)
        nums.sort()
        while cm<n:
            if nums[cm]==nums[cm-1]:
                return True
            else:
                nums[off+1]=nums[cm]
                off+=1
                cm+=1
        return False