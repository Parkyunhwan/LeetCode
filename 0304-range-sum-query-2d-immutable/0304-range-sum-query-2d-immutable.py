class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.box = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.box[i][j] = matrix[i - 1][j - 1] + self.box[i - 1][j] + self.box[i][j -1] - self.box[i - 1][j - 1]
        

    def sumRegion(self, row1, col1, row2, col2):    
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.box[r2][c2] - self.box[r1 - 1][c2] - self.box[r2][c1 - 1] + self.box[r1 - 1][c1 - 1]