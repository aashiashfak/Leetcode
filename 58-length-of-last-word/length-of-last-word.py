class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split(' ')
        a = len(words[-1])
        print(a)
        return a