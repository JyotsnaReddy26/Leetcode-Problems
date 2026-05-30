class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        new=[[-1]*col for i in range(row)]
       
        for i in range(row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    for m in range(0,col):
                        new[i][m]=0
                    for n in range(0,row):
                        new[n][j]=0
        
        for i in range(row):
            for j in range(col):
                if new[i][j]==0:
                    matrix[i][j]=0
