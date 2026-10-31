class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        queue=[]
        for i in nums:
            queue.append(-i)
        heapq.heapify(queue)
        for i in range(k-1):
            heapq.heappop(queue)
        return -heapq.heappop(queue)