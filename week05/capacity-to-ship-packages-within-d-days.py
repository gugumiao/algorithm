class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid = (start + end)//2
            cd = self.countDays(mid, weights)
            if cd > days:
                start = mid + 1
            else:
                end = mid
        return start


    def countDays(self, target, weights):
        cd = 1
        current = 0
        for weight in weights:
            current += weight
            if current > target:
                cd += 1
                current = weight
        return cd

