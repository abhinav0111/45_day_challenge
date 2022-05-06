class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rl = []
        ml = []
        for i in range(len(matrix[0])):
            k = []
            f = 1
            for j in range(len(matrix)):
                if f == 0:
                    if matrix[j][i] == 0:
                        rl.append(j)
                    ml.append([j, i])
                else:
                    if matrix[j][i] != 0:
                        k.append(j)
                        k.append(i)
                    else:
                        rl.append(j)
                        if len(k) != 0:
                            ml.append(k)
                        f = 0
        for i in range(len(ml)):
            if len(ml[i]) > 2:
                for j in range(0, len(ml[i])-1, 2):
                    matrix[ml[i][j]][ml[i][j+1]] = 0
            else:
                matrix[ml[i][0]][ml[i][1]] = 0
        for i in rl:

            matrix[i] = [0]*(len(matrix[0]))
