from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        l = r = 0

        while r < len(nums):
            # Remove smaller elements from the back of the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove indices that are out of the current window left boundary
            if l > q[0]:
                q.popleft()

            # Once the window has reached size k, record the max and slide the left pointer
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1

        return output