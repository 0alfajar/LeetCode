class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = requests[0]
        floor = requests[0]
        for i in range(1, len(requests)):
            diff = abs(requests[i] - requests[i-1])
            time += diff
            floor = diff
        return time
