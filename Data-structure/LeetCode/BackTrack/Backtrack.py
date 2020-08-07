# Time：2020/6/2411:22
class SolutionOne:
    def __init__(self, nums=[1, 2, 2]):

        self.temp = []
        self.result_ = []
        self.nums = nums

    def subsets(self):
        self.recursion_help(0, self.temp, self.result_)
        return self.result_

    def recursion_help(self, i, temp, result):

        if i == len(self.nums):
            result.append(temp)
            return

        self.recursion_help(i+1, temp+[self.nums[i]], result)  # 选择该元素
        self.recursion_help(i+1, temp, result)                 # 不选择该元素


class SolutionTwo:
    """
    N皇后问题(回溯+递归)实现
    """
    def __init__(self, n):
        self.n = n
        self.dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        self.dy = [0, 0, -1, 1, -1, 1, -1, 1]
        self.mark = [[0]*self.n for i in range(self.n)]
        self.location = [["."]*self.n for j in range(self.n)]
        self.result = []

    def put_down_the_queue(self, x, y, mark):
        mark[x][y] = 1
        for i in range(1,self.n):
            for j in range(self.n):
                new_x = x + i * self.dx[j]
                new_y = y + i * self.dy[j]

                if new_x >= 0 and new_y >= 0 and new_x < self.n and new_y < self.n:
                    mark[new_x][new_y] = 1

    def demo(self):
        self.put_down_the_queue(3, 3, self.mark)
        for i in self.mark:
            print(i, end="\n")

    def solve_n_queues(self):
        self.generate(0,self.n,self.location,self.result,self.mark)
        return self.result

    def generate(self,k,n,location,result,mark):
        if k == n:
            result.append(location)
            return
        for i in range(n):
            if mark[k][i] == 0:
                temp_mark = mark.copy()
                location[k][i] = "Q"
                self.put_down_the_queue(k,i,mark)
                self.generate(k+1,n,location,result,mark)
                mark = temp_mark
                location[k][i] = "."


if __name__ == '__main__':
    # solution = SolutionOne()
    # val = solution.subsets()
    # print(val)

    solution = SolutionTwo(4)
    res = solution.solve_n_queues()
    print(res)