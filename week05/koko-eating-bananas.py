class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n, maxp = len(piles), max(piles)
        sump = sum(piles)
        if n == h:
            return maxp

        left, right = (sump-1) // h + 1, min(maxp, sump // (h-n))
        while left < right:
            mid = (left+right) // 2
            time = 0
            for pile in piles:
                time += (pile-1) // mid + 1
                if time > h:
                    left = mid + 1
                    break
            if time <= h:
                right = mid
        return left

