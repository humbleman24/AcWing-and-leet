n = int(input())
a = list()
# 只考虑了单次变化的可能，应考虑到添加之后的动态变化过程
# for i in range(n):
#     b = list(map(int,input().split()))
#     add = False
#     if a:
#         for l,r in a:
#             if b[0] <= r:
#                 if b[1] > r:
#                     r = b[1]
#                     add = True
#                     break
#             if b[0] <= l:
#                 if b[1] >= l:
#                     l = b[0]
#                     add = True
#                     break
#         if not add:
#             a.append(b)   
#     else:
#         a.append(b)


for i in range(n):
    b = list(map(int,input().split()))
    j = 0
    while j < len(a):                      # 考虑添加新元素的位置
        if a[j][0] < b[0]:                 # 按照左端点的大小排序        
            j += 1
        elif a[j][0] == b[0]:              # 相等时要考虑右端点
            if a[j][1] < b[1]:
                j += 1
            else:
                break
        else:                              # 及时出去
            break
    a.insert(j,b)

    k = 0
    while k < len(a)-1:                     # 合并区间
        if a[k][1] >= a[k+1][0]:            # 唯一需要合并的情况
            if a[k][1] < a[k+1][1]:         # 考虑大区间完全包含小区间的情况
                a[k][1] = a[k+1][1]
            a.pop(k+1)
        else:
            k += 1

print(len(a))