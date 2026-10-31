class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        queue=[]
        for i in stones:
            queue.append(-i)
        heapq.heapify(queue)
        while len(queue)>1:
            a=-heapq.heappop(queue)
            b=-heapq.heappop(queue)
            if (a-b)!=0:
                heapq.heappush(queue,-(a-b))
        if queue:
            return -queue[0]
        else:
            return 0