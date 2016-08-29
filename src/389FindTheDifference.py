# Definition for a binary tree node.
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        dict_s = {}
        dict_t = {}
        for i in range(0,len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] +=1
            else:
                dict_s[s[i]] =1
            if t[i] in dict_t:
                dict_t[t[i]] +=1
            else:
                dict_t[t[i]] =1
        if t[len(t)-1] in dict_t:
            dict_t[t[len(t)-1]] +=1
        else:
            dict_t[t[len(t)-1]] =1
        for j in dict_t:
            if j not in dict_s:
                return j
            if dict_s[j] != dict_t[j]:
                return j


train = Solution()
s = "abcd"
t = "abcde"
print train.findTheDifference(s,t)
