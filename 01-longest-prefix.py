"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        for i in range(len(strs[0])):
            letter = strs[0][i]
            try:
                other_letters = [st[i] for st in strs]
            except:
                break
            if all(l == letter for l in other_letters):
                longest_prefix += letter
            else:
                break

        return longest_prefix
    
if __name__ == "__main__":
    strs_1 = ["flower","flow","flight"]
    strs_2 = ["dog","racecar","car"]

    solution = Solution()

    answer1 = solution.longestCommonPrefix(strs_1)
    answer2 = solution.longestCommonPrefix(strs_2)
