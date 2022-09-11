class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        # storing the maximum
        mx = 0
        # stores the running sum of the k-1 fastest runners with
        # the same or better efficiency than the current runner
        # plus the speed of the current runner.
        speed_sum = 0
        # stores the speeds of the fastest k engineers.
        # is used as min-heap to easily pop off the slowest engineers from the list
        fastest_k = []
        # by sorting by efficiency first and decreasing, it's enforced,
        # that all fastest engineers in "fastest_k" have the same or higher
        # efficiency than the currently handled one
        for eff, spe in sorted(zip(efficiency, speed), reverse = True):
            if len(fastest_k) == k:
                # if the array already holds k entries, we need one more space to
                # include the current engineer. The now popped engineers speed needs to
                # be subtracted from the current speed_sum, as they won't be on the team anymore
                speed_sum -= heappop(fastest_k)
            # current engineer might not be the fastest, but needs to be considered for it's speed,
            # because they are currently the fixed part. If they can't compete speedwise, they will be popped
            # when considering the next engineer.
            heappush(fastest_k, spe)
            # the current engineer is fixed to be part of the team, so their speed needs to be 
            # added to the speed_sum
            speed_sum += spe
            # check, if the fastest engineers plus the current one will perform better than any other team yet
            mx = max(mx, speed_sum * eff)
        # return mod 1**9 + 7 because they said so in the description lmao
        return mx  % mod