# @Time：2020/6/269:10


def update(num, result_):
    num = num+100
    result_[0] = result_[0]+100


if __name__ == '__main__':
    num01 = 100
    result = [11,12,13]
    update(num01,result)
    print(num01)
    print(result)
    print(10 % -3)