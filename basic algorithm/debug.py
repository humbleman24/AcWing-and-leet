N = 100010
e = [0] * N
left = [0] * N
right = [0] * N
head = -1
tail = -1
idx = 0

def add_l(val):
    global head,tail,idx
    if head != -1:
        e[idx] = val
        right[idx] = head
        left[idx] = -1
        left[head] = idx
        head = idx
        
    elif head == -1:
        e[idx] = val
        right[idx] = head
        left[idx] = -1
        head = idx
        tail = idx
    idx += 1

def add_r(val):
    global head,tail,idx
    if tail != -1:
        e[idx] = val
        left[idx] = tail
        right[idx] = -1
        right[tail] = idx
        tail = idx
    elif tail == -1:
        e[idx] = val
        left[idx] = tail
        right[idx] = -1
        tail = idx
        head = idx
    idx += 1

def delete_node(i):
    global head,tail,idx
    left[right[i]] = left[i]
    right[left[i]] = right[i]

    if head == i:
        head = left[head]
    if tail == i:
        tail = right[tail]

def insert_l(i,val):
    global head,tail,idx
    e[idx] = val
    right[idx] = i
    left[idx] = left[i]
    right[left[i]] = idx
    left[i] = idx
    if head == i:
        head = idx
    idx += 1

def insert_r(i,val):
    global head,tail,idx
    e[idx] = val
    right[idx] = right[i]
    left[idx] = i
    left[right[i]] = idx
    right[i] = idx
    if tail == i:
        tail = idx
    idx += 1

def traversal():
    current = head
    while current != -1:
        print(e[current],end=' ')
        current = right[current]
    print()
 
M = int(input())
for i in range(M):
    operant = input().split()
    if operant[0] == 'L':
        add_l(operant[1])
    elif operant[0] == 'R':
        add_r(operant[1])
    elif operant[0] == 'IL':
        insert_l(int(operant[1])-1,operant[2])
    elif operant[0] == 'IR':
        insert_r(int(operant[1])-1,operant[2])
    elif operant[0] == 'D':
        delete_node(int(operant[1])-1)
    traversal()

