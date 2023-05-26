# Dictionaries
print('Dictionaries')

# Standard Dictionaries 是無序的，這代表當每次我操作字典時，都會需要遍歷整個字典，且無法保證順序
# 在 collections module 中的 OrderedDict 則是一種特殊的有序字典，會紀錄每個 key-value pair 的插入順序

# 情境一：當我要添加一個新的 key-value pair 時，因為不知道字典中是否已經存在該 key，所以我們需要先判斷是否存在，若不存在則添加，
# 若存在則更新 value
# By Standard Dictionaries
print('By Standard Dictionaries')
dict = {}
key = 'counter'
if key not in dict:
    dict[key] = 0
dict[key] += 1
print(dict)

# By defaultdict
# collections module 中的 defaultdict 可以讓我們在初始化字典時，就指定一個 default value，當我們要添加一個新的 key-value pair 時，
# 若該 key 不存在，則會自動添加並指定 default value 給該 key
print('By defaultdict')
from collections import defaultdict

dict = defaultdict(int)
dict['counter'] += 1
print(dict)

print('----------------------------------------')

# Queue, Stack, and Heap
print('Queue, Stack, and Heap')
# Queue and Stack 是一個 dynamic lists，其中 DELETE 在 Queue 是從 list 的頭部刪除，而 Stack 則是從 list 的尾部刪除。
# 因為 PUSH 和 POP 的操作會需要 O(1) 的時間，所以我們可以使用 list 來實現 Queue 和 Stack。

# Queue: FIFO (First In First Out)，可以用來實現 BFS (Breadth-First Search)。
print('Queue: FIFO (First In First Out)')
queue = []
queue.insert(0, 1)
queue.insert(0, 2)
queue.insert(0, 3)
print(queue)
queue.pop()
print(queue)

# Stack: LIFO (Last In First Out)，可以用來實現 DFS (Depth-First Search)。
print('Stack: LIFO (Last In First Out)')
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
print(stack)

# Deque: 雙向 Queue，可以在頭部和尾部都執行 PUSH 和 POP 的操作。
print('Deque: 雙向 Queue')
from collections import deque

fifo = deque()
fifo.append(1)
fifo.append(2)
fifo.append(3)
print(fifo)
fifo.popleft()
print(fifo)

lifo = deque()
lifo.append(1)
lifo.append(2)
lifo.append(3)
print(lifo)
lifo.pop()
print(lifo)

# Heap: 一種特殊的樹狀結構，其中每個節點的值都大於等於其子節點的值，可以用來實現優先級隊列 (Priority Queue)。
# A[Parent(i)] >= A[i]
# heapq from collections module is an implementation of heap
print('Heap: 一種特殊的樹狀結構')

from heapq import heappush, heappop, nsmallest

heap = []
heappush(heap, 5)
heappush(heap, 2)
heappush(heap, 3)
heappush(heap, 1)
heappush(heap, 4)
print(heappop(heap), heappop(heap), heappop(heap), heappop(heap), heappop(heap))
heappush(heap, 5)
heappush(heap, 2)
heappush(heap, 3)
heappush(heap, 1)
heappush(heap, 4)

print(heap[0], nsmallest(1, heap)[0])
assert heap[0] == nsmallest(1, heap)[0] == 1

# Linked List: 一種特殊的 list，其中每個節點都包含了下一個節點的指針。
# 限制：
# 1. 沒有辦法直接訪問第 k 個元素，需要從頭部開始遍歷 k 次才能訪問到第 k 個元素。
# 2. 沒有辦法直接訪問最後一個元素，需要從頭部開始遍歷整個 list 才能訪問到最後一個元素。
# 3. 沒有辦法直接在中間插入一個元素，需要先找到要插入的位置，然後將該位置的節點指針指向新的節點，再將新的節點指針指向原本該位置的下一個節點。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None  # 指向下一個節點的指針

pointer = head = ListNode(None)
while pointer.next:
    print(pointer.val)
    pointer = pointer.next
print(pointer.val)
