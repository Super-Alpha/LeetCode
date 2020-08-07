# Time：2020/6/2411:21

def generate(item, left, right, result):

    if left == 0 and right == 0:
        result.append(item)
        return
    if left > 0:
        generate(item+"(", left-1, right, result)
    if left < right:
        generate(item+")", left, right-1, result)


if __name__ == '__main__':
    res = []
    generate("", 2,2, res)
    print(res)
