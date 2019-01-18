class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for j in J:
            for s in S:
                if j == s:
                    count += 1
        print(count)
        return count
