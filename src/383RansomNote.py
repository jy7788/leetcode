# Definition for a binary tree node.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(ransomNote)>len(magazine):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(0,len(ransomNote)):
            if ransomNote[i] in dict_s:
                dict_s[ransomNote[i]] +=1
            else:
                dict_s[ransomNote[i]] =1
            if magazine[i] in dict_t:
                dict_t[magazine[i]] +=1
            else:
                dict_t[magazine[i]] =1
        for j in range(len(ransomNote),len(magazine)):
            if magazine[j] in dict_t:
                dict_t[magazine[j]] +=1
            else:
                dict_t[magazine[j]] =1
        for j in dict_s:
            if j not in dict_t:
                return False
            if dict_s[j] > dict_t[j]:
                return False
        return True


train = Solution()
s = "aa"
t = "aab"
print train.canConstruct(s,t)
