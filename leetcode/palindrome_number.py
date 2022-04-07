class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        new_num = num[::-1]
        if num == new_num:
            return True
        else:
            return False