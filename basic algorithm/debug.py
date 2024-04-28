N = 100010
arr = [0] * N
point = 0
first = -1

M = int(input())

for i in range(M):
    command = input().split()
    if command[0] == 'push':
        arr[point] = command[1]
        point += 1
    elif command[0] == 'pop':
        first += 1
    elif command[0] == 'empty':
        if point - first == 1:
            print('yes')
        else:
            print('no')
    elif command[0] == 'query':
        print(arr[first+1])