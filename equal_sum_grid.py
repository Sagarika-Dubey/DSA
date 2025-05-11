class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total= sum(sum(i) for i in grid)
        if total%2!=0:
            return False

        row_sum=[sum(row) for row in grid]
        curr_sum=0

        for i in range(len(row_sum)-1):
            curr_sum+=row_sum[i]
            if curr_sum== total//2:
                return True

        col=len(grid[0])
        col_sum=[0]*col
        for i in range (len(grid)):
            for j in range(col):
                col_sum[j] +=grid[i][j]

        curr_sum=0
        for i in range(col-1):
            curr_sum+=col_sum[i]
            if curr_sum== total//2:
                return True

        return False
            