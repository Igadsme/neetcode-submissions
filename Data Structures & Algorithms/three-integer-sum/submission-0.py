class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers if we want a sum of 0, since sorted array means no more zeros can be formed
            if a > 0:
                break

            # Skip duplicate elements for the first number to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate elements for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res