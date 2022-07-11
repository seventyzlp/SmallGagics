def conflict(state, nextColumn):
    nextRow = rows = len(state)  # 5
    for row in range(rows):  # 0,1,2,3,4
        # 获取当前行的列
        column = state[row]
        if abs(column - nextColumn) in [0, nextRow - row]:
            return True
    return False


# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置
def queens(num, state=()):
    # 每一行的列坐标都是从0:7的
    # 0,1,2,3,4,5,6,7
    for pos in range(num):
        # 默认state为空。长度为0，但是是不冲突的
        # 判断是否冲突，state为空时不冲突
        if not conflict(state, pos):  # 回溯法的体现
            # 如果state的长度为7，即到达了倒数第二行，也就是前7行皇后都已经找到了位置，最后一行又没有冲突，返回最后一行的列坐标
            if len(state) == num - 1:
                # 最后一行的（pos,）=最后一行的result，然后再递归回去求倒数第二行的result
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '.' * (pos) + 'X' + '.' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


solutions = queens(8)
for index, solution in enumerate(solutions):
    print('第%d种解决方案：' % (index + 1), solution)
    prettyprint(solution)
    print('*' * 50)
