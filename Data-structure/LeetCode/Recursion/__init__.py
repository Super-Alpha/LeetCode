# Time：2020/6/2411:24
"""public class Queue8 {

int max = 8;
int[] array = new int[max];

// 放置第n个皇后
private void check(int n) {
if (n == max) {
print();
return;
}
// 从第一列开始摆放
for (int i = 0; i < max; i++) {
array[n] = i;
if (judge(n)) {
check(n+1);
}
}
}

// 判断当前摆放的皇后和之前摆放的皇后是否冲突
private
boolean
judge(int
n) {
for (int i=0; i < n;i++) {
if (array[i] == array[n] | | Math.abs(n - i) == Math.abs(array[n] - array[i])) {
return false;
}
}
return true;
}
}"""
class Solution:
    def __init__(self,n):
        self.n = n
        self.array = [0]*n
        self.res = []
        self.temp = ["."*n for i in range(n)]

    def solve(self):
        self.check(0)

    def check(self, n):
        if n == self.n:
            for index, val in enumerate(self.array):
                print([index,val])
                self.temp[index].replace(self.temp[index][val],"Q")
            self.res.append(self.temp)
            return
        for i in range(self.n):
            self.array[n] = i
            if self.judge(n):
                self.check(n+1)

    def judge(self,n):
        for i in range(n):
            if self.array[i] == self.array[n] or abs(n-i) == abs(self.array[n] - self.array[i]):
                return False
        return True


def three_sum_closest(nums=[1, 1, 1, 0], target=1):
    nums.sort()
    n = len(nums)
    best = 10**7

    def update(current):
        nonlocal best
        if abs(current-target) < abs(best-target):
            best = current

    for pa_ in range(n):
        # 保证和上一次枚举的元素不相同
        if pa_ > 0 and nums[pa_] == nums[pa_-1]:
            continue
        pb_ = pa_+1
        pc_ = n - 1
        while pb_ < pc_:
            temp = nums[pa_] + nums[pb_] + nums[pc_]
            if temp == target:
                return temp
            update(temp)
            if temp > target:
                # 如果和大于target，左移动c对应的指针
                t1 = pc_ - 1
                # 移动到下一个不相等的元素
                while pb_ < t1 and nums[t1] == nums[pc_]:
                    t1 -= 1
                pc_ = t1
            else:
                # 如果和小于target，右移动b对应的指针
                t2 = pb_ + 1
                # 移动到下一个不相等的元素
                while t2 < pc_ and nums[t2] == nums[pb_]:
                    t2 += 1
                pb_ = t2
    return best
#print(three_sum_closest())


if __name__ == '__main__':
    # s = Solution(4)
    # s.solve()
    # print(s.res)
    s=[3,3,3]
    print(min(s))

