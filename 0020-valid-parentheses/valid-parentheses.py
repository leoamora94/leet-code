class Solution:
    def isValid(self, s: str) -> bool:
        options = dict(('()', '[]', '{}'))
        compare = []

        for i in s:
            if i in '([{':
                compare.append(i)
            elif len(compare) == 0 or i != options[compare.pop()]:
                return False

        return len(compare) == 0
