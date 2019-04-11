class Solution:
    end = 1
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 : return 0
        if len(s) == 1 : return 1
        begin = 0
        max_length = 1
        for self.end in range(1,len(s)):
            if s[self.end] in s[begin:self.end] :
                max_length = max(max_length, self.end - begin)
                while begin != self.end:
                    if s[self.end] not in s[begin:self.end] :
                        break 
                    begin += 1
        max_length = max(max_length, self.end - begin + 1)
        return max_length
