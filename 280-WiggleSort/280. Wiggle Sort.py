__author__ = 'liuxiyun'
# The idea is, first sort the list, then exchange each two from the second element
# nlogn
    def wiggleSort(self, nums):# no extra space
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        nums.sort()
        i,j=1,2
        while i<len(nums) and j<len(nums):
            nums[i],nums[j] = nums[j],nums[i]
            i+=2
            j+=2
# The idea is, check each three that should satisfy ACB, if not, exchange the middle element with the largger one between it's side
# O(n)
    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        i=1
        while i<len(nums)-1:
            if nums[i-1]<=nums[i]>=nums[i+1] :
                pass
            elif nums[i-1]<nums[i+1]:
               nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
               nums[i],nums[i-1] = nums[i-1],nums[i]
            i+=2
        if len(nums)%2 ==0:
            if nums[-2]>nums[-1]:
                nums[-2],nums[-1] = nums[-1],nums[-2]
                return
        else:
            return
# discussion:
# O(n)
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        for i in range(len(nums)):
            if i%2 == 1 and nums[i]<=nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
            if i!=0 and i%2 == 0 and nums[i]>=nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
