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
    
    def lengthOfLongestSubstringSolution(self, s: str) -> int:
        myset = set()  # Store unique characters
        left = 0  # Left pointer of the window
        max_length = 0

        for right in range(len(s)):  # Right pointer expands the window
            while s[right] in myset:  # If duplicate found, shrink window
                myset.remove(s[left])
                left += 1

            myset.add(s[right])  # Add the new character to the set
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
    
print(Solution().lengthOfLongestSubstringSolution('pwwwk'))

# print(Solution.lengthOfLongestSubstring('aab'))
# print(Solution.lengthOfLongestSubstring('abcabcbb'))
# print(Solution.lengthOfLongestSubstring('bbbbb'))
# print(Solution.lengthOfLongestSubstring('pwwkew'))