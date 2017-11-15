# 生成器实例，当需要的数据用比较复杂的算法实现，就不能用data = (x for x in [])这样的方式实现。
# generator保存的是算法，return返回的全部数据，数据量大，吃内存。
# @2017/11/15

def triangles():
    L = [1]
    yield L
    L = [1,1]
    yield L
    while 1:
        for j in range(0,len(L)):
            if j == 0:
                La = [1,]
            else:
                La.append(L[j] + L[j-1])
            if j == len(L) - 1:
                La.append(1)
        L = La
        yield L
n = 0 # 行数
for t in triangles():
    print(t)
    n += 1
    if n == 100:
        break
