from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sorted_list = sorted(strs)

        first = sorted_list[0]
        last = sorted_list[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            else:
                prefix += first[i]

        return prefix
