
# 获取列表中执行元素出现第N次对应的下标
def get_index(l, x, n):
    counts = l.count(x)
    num = 0
    result = None
    if n <= counts:

        for item in enumerate(l):
            if item[1] == x:
                num +=1
            if num == n:
                result = item[0]
                break
    return result