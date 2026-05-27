class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p_Triangle=[]
        for i in range(numRows):
            currentRow=[1]*(i+1)
            for j in range(1,i):
                currentRow[j] = p_Triangle[i - 1][j - 1] + p_Triangle[i - 1][j]
            p_Triangle.append(currentRow)

        return p_Triangle