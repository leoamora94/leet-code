class Solution:
    def reverse(self, x: int) -> int:
        invert = []
        is_neg = False

        if x < 0:
            x *= -1
            is_neg = True

        x = str(x)

        for i in range(len(x)):
            if x[i] in "0123456789":
                invert.insert(0, x[i])

        temp = invert.copy()

        for i in range(len(temp)):
            if invert[i] == 0:
                invert.pop(i)

        answer = int("".join(invert))

        if answer > (2**31 - 1) or answer < -(2**31):
            return 0

        if is_neg:
            return -answer
        return answer