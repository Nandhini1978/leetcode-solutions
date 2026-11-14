class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        indeg=[0]*(n+1)
        outdeg=[0]*(n+1)
        for u,v in trust:
            indeg[v]+=1
            outdeg[u]+=1
        for i in range(1,n+1):
            if indeg[i]==n-1 and outdeg[i]==0:
                return i
        return -1
