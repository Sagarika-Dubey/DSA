class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dp = [[float('inf')] * m for _ in range(n)]
        minh = []
        heapq.heappush(minh, (0, 0, 0))
        moveTime[0][0] = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while minh:
            currTime, currRow, currCol = heapq.heappop(minh)
            if currTime >= dp[currRow][currCol]:
                continue
            if currRow == n - 1 and currCol == m - 1:
                return currTime
            dp[currRow][currCol] = currTime
            for dr, dc in directions:
                nextRow = currRow + dr
                nextCol = currCol + dc
                if 0 <= nextRow < n and 0 <= nextCol < m and dp[nextRow][nextCol] == float('inf'):
                    cost=(currRow+currCol)%2+1
                    start= max(moveTime[nextRow][nextCol], currTime)
                    nextTime = cost+start
                    heapq.heappush(minh, (nextTime, nextRow, nextCol))
        return -1