class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degrees = []
        for node in matrix:
            degree = sum(node)
            degrees.append(degree)
        return degrees