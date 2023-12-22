class Solution:
    def romanToInt(self, s: str) -> int:
        # if next I has V or X, dont count
        # If next X has L or C, dont count
        # If next C has D or M, dont count
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ansr = 0

        for i in range(len(s)):
            if i < len(s)-1 and numbers[s[i]] < numbers[s[i+1]]:
                ansr -= numbers[s[i]]
            else:
                ansr += numbers[s[i]]

        return ansr
