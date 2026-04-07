class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        friends = set(friends)
        for position in order:
            if(position in friends):
                result.append(position)
        return result
        