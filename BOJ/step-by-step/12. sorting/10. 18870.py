# 18870 μ’ν μμΆ

N = int(input())
datas = list(map(int, input().split()))
s_datas = sorted(list(set(datas)))
d = {s_datas[i] : i for i in range(len(s_datas))}
for data in datas:
    print(d[data], end=' ')