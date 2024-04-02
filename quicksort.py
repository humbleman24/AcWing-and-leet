# roughly wrong one
def quicksort1(n,lst):
    if n < 2:
        return lst
    p = n-1
    l = 0
    r = n-2
    while l != r:
        if lst[l] <= lst[p]:
            l += 1
        else:
            if lst[r] >= lst[p]:
                r -= 1
            else:
                lst[l], lst[r] = lst[r], lst[l]
    if lst[p] < lst[l]:
        lst[p], lst[l] = lst[l], lst[p]
        lst[0:l] = quicksort1(l, lst[0:l])
        lst[l+1:n] = quicksort1(n-l-1,lst[l+1:n])
    else:
        lst[0:l+1] = quicksort1(l+1, lst[0:l+1])
        lst[l+1:n] = quicksort1(n-l-1,lst[l+1:n])
    return lst

def quicksort2(array):
    if len(array) < 2:
        return array

    # 选择最后一个元素作为基准值
    pivot_index = len(array) - 1
    pivot_value = array[pivot_index]

    # 用两个指针分割列表
    left_index = 0
    right_index = len(array) - 2

    while left_index <= right_index:
        # 在左侧找到第一个比基准值大的元素
        while array[left_index] < pivot_value:
            left_index += 1

        # 在右侧找到第一个比基准值小的元素
        while right_index >= 0 and array[right_index] > pivot_value:
            right_index -= 1

        # 交换两个指针所指向的元素
        if left_index <= right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
            right_index -= 1

    # 将基准值移到正确的位置
    array[pivot_index], array[left_index] = array[left_index], array[pivot_index]

    # 递归排序左右两个子列表
    left = quicksort2(array[:left_index])
    right = quicksort2(array[left_index+1:])

    # 返回排序后的列表
    return left + [pivot_value] + right

def quicksort3(q,l,r):
    if l >= r:
        return 
    i = l-1
    j = r+1
    x = q[l+r>>1]  # right shift operator, same as divided by two. Finding the middle index of the array
    while i < j:
        i += 1
        while q[i] < x:
            i += 1
        j -= 1
        while q[j] > x:
            j -= 1
        
        if i < j:
            q[i], q[j] = q[j], q[i]
        
    quicksort3(q,l,j)
    quicksort3(q,j+1,r)


n = int(input())
q = list(map(int,input().split()))

quicksort3(q,0,n-1)
print(''.join(map(str,q)))