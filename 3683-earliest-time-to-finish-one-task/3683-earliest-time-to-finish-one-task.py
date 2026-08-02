class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        time_task = [sum(task) for task in tasks]
        return min(time_task)
        