class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        myset = set()
        counter: int = 0
        maxx: int = 0

        for elem in s:
            if (elem in myset):
                maxx = max(maxx, counter)
                counter = 0;
                myset.clear()
                myset.add(elem)
                counter = counter + 1
            else:
                myset.add(elem)
                counter = counter + 1
        maxx = max(maxx, counter)
        return maxx
        

print(Solution.lengthOfLongestSubstring('aab'))
print(Solution.lengthOfLongestSubstring('abcabcbb'))
print(Solution.lengthOfLongestSubstring('bbbbb'))
print(Solution.lengthOfLongestSubstring('pwwkew'))