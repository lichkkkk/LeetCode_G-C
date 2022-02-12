class SparseVector:    
    def __init__(self, nums: List[int]):
        self.values_dict = {i: n for i, n in enumerate(nums) if n != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        common_i = set(vec.values_dict.keys()) & set(self.values_dict.keys())
        return sum(self.values_dict[i] * vec.values_dict[i] for i in common_i)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
