class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        count = 0
        for s in S:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        for j in J:
            if j in dic:
                count += dic[j]
        print(count)
        return count