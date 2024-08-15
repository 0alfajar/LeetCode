class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5 = 0
        change_10 = 0

        for bill in bills:
            if bill == 5:
                change_5 += 1
            elif bill == 10:
                if change_5 < 1:
                    return False
                change_5 -= 1
                change_10 += 1
            else:  # bill == 20
                if change_10 >= 1 and change_5 >= 1:
                    change_10 -= 1
                    change_5 -= 1
                elif change_5 >= 3:
                    change_5 -= 3
                else:
                    return False
        return True