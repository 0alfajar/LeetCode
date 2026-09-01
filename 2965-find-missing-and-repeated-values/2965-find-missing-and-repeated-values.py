class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing_repeated = []

        flatten_arr = [item for subgrid in grid for item in subgrid]

        freq_arr = {}

        for i in range(len(flatten_arr)):
            if flatten_arr[i] not in freq_arr:
                freq_arr[flatten_arr[i]] = 1
            else:
                missing_repeated.append(flatten_arr[i])
        
        for i in range(1, len(flatten_arr)+1):
            if i not in flatten_arr:
                missing_repeated.append(i)

        return missing_repeated

