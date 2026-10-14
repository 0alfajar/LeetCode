class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
          t0 = startTime.split(":")
          t1 = endTime.split(":")

          t0_s = int(t0[0]) * 3600 + int(t0[1]) * 60 + int(t0[2])
          t1_s = int(t1[0]) * 3600 + int(t1[1]) * 60 + int(t1[2]) 

          return abs(t0_s - t1_s)