class Solution:
    def __init__(self, s):
        self.s = s
    def lengthOfLongestSubstring(self):
        """
        :type s: str
        :rtype: int
        """
        sub = {}
        cur_sub_start = 0 
        cur_len = 0
        longest = 0 
        for i, letter in enumerate(self.s):
            #check duplicate and update when substring is longer than before 
            if letter in sub:
                cur_len = i - sub[letter] #check the length
                sub[letter] = i 
            #increasing length of a substring if there is no duplicate
            else:
                sub[letter] = i
                cur_len += 1 
                #when substring is longest than update the longest
                if cur_len > longest:
                    longest = cur_len
        return longest

if __name__ == '__main__':
    s = 'abcabcbb'
    case1 = Solution(s)
    print(case1.lengthOfLongestSubstring())