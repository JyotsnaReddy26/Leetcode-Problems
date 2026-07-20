class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        
        flat = []
        for row in grid:
            for num in row:
                flat.append(num)

        total = m * n
        k %= total  
        
        shifted = flat[-k:] + flat[:-k]  
        
        result = []
        index = 0
        for i in range(m):
            row = shifted[index : index + n]
            result.append(row)
            index += n

        return result