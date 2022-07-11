import turtle


def check(state, nextColumn):
    nextRow = rows = len(state)  # 5
    for row in range(rows):  # 0,1,2,3,4
        # 获取当前行的列
        column = state[row]
        if abs(column - nextColumn) in [0, nextRow - row]:
            return True
    return False


# 生成皇后位置
def queens(num, state=()):
    for pos in range(num):
        # 默认state为空。长度为0，但是是不冲突的
        # 判断是否冲突，state为空时不冲突
        if not check(state, pos):  # 回溯法
            if len(state) == num - 1:
                # 最后一行的（pos,）=最后一行的result，然后再递归回去求倒数第二行的result
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):  # 生成输出
    def line(pos, length=len(solution)):
        return '.' * (pos) + 'X' + '.' * (length - pos - 1)
    for pos in solution:
        print(line(pos))


n = int(input("请输入皇后的数量:"))
solutions = queens(n)
for index, solution in enumerate(solutions):
    print('第%d种解决方案：' % (index + 1), solution)
    prettyprint(solution)
    print('*' * 50)
