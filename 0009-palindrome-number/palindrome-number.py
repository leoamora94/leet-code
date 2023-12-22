class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digit = x
        reverse = 0

        while digit != 0:
            resto = digit % 10
            reverse = reverse*10 + resto
            digit = digit // 10

        return reverse == x
