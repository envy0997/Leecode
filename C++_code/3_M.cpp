class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        using namespace std;
        int i, end = 1;
        int begin = 0;
        int max_length = 1;
        if (s.length() == 0) return 0;
        if (s.length() == 1) return 1;
        for (end; end < s.length(); end++) {
            for (i = begin; s[i] != s[end]; i++);
            if (i != end) {
                max_length = (end - begin) > max_length ? (end - begin) : max_length;
                begin = i + 1;
            }
        }
        max_length = (end - begin) > max_length ? (end - begin) : max_length;
        return max_length;
    }
};