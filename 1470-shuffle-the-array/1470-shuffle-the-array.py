class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[0:n]
        nums2 = nums[n:2*n]

        shuffle_arr = []
        for i in range(n):
            shuffle_arr.append(nums1[i])
            shuffle_arr.append(nums2[i])
        
        return shuffle_arr