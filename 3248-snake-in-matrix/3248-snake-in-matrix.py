class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = 0
        j = 0
        for command in commands:
            if command == 'UP':
                i -= 1
            if command == 'DOWN':
                i += 1
            if command == 'RIGHT':
                j += 1
            if command == 'LEFT':
                j -= 1
        return (i * n) + j