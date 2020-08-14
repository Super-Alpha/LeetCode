# @Time：2020/8/118:39
class Solution:

    def solveNQueens(self,n):
        # 判断该位置的列、主对角线、次对角线是否满足要求
        def could_place(row,col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        # 放置皇后，并将皇后所处的列、主对角线、次对角线置1
        def place_queen(row,col):
            queens.add((row,col)) # 记录皇后的位置
            cols[col] = 1  # 代表皇后所处的一整列
            hill_diagonals[row - col] = 1  # 代表皇后所处的整个主对角线
            dale_diagonals[row + col] = 1  # 代表皇后所处的整个次对角线

        # 回溯，将在(row，column)方格的皇后移除
        def remove_queen(row,col):
            queens.remove((row,col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        # 将皇后的位置，转换为符合输出的格式
        def add_solution():
            solution = []
            for _,col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        # 摆放皇后
        def backtrack(row=0):
            for col in range(n):
                if could_place(row,col):
                    place_queen(row,col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1) # 摆放第row+1行的皇后，若无恰当位置摆放，则进行回溯
                    remove_queen(row,col)  # 开始回溯，移除摆放的皇后，执行循环，跳跃到下一个列的位置，再验证

        cols = [0] * n  # 其中的元素代表皇后所处位置的整个列
        hill_diagonals = [0] * (2 * n - 1)  # 其中的每一个元素代表一整条主对角线
        dale_diagonals = [0] * (2 * n - 1)  # 其中的每一个元素代表一整条次对角线
        queens = set()
        output = []
        backtrack()
        return output

if __name__ == '__main__':

    solution = Solution()
    res=solution.solveNQueens(4)
    print(res)
