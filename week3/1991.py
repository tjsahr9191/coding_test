import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

head = Node('A', None, None)

def insertNode(head, root, left, right):

    if head is None:
        return

    if head.data == root:
        head.left = None if left == '.' else Node(left, None, None)
        head.right = None if right == '.' else Node(right, None, None)
    else:
        insertNode(head.left, root, left, right)
        insertNode(head.right, root, left, right)

def pre_order(head):

    if head == None:
        return

    print(head.data, end = '')
    pre_order(head.left)
    pre_order(head.right)

    return

def in_order(head):

    if head == None:
        return

    in_order(head.left)
    print(head.data, end = '')
    in_order(head.right)

    return

def post_order(head):
    if head == None:
        return

    post_order(head.left)
    post_order(head.right)
    print(head.data, end = '')

    return

n = int(input())
for _ in range(n):
    root, left, right = input().split()

    insertNode(head, root, left, right)

pre_order(head)
print()
in_order(head)
print()
post_order(head)

