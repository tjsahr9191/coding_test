import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def insert_node(tree, n):
    if tree is None:
        return

    if tree.data > n:
        if tree.left == None:
            tree.left = Node(n, None, None)
        else:
            insert_node(tree.left, n)
    elif tree.data < n:
        if tree.right == None:
            tree.right = Node(n, None, None)
        else:
            insert_node(tree.right, n)

def post_order(tree):

    if tree is None:
        return

    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)

tree = Node(0, None, None)

while True:
    n = input()
    if n == '':
        break

    n = int(n)

    if tree.data == 0:
        tree = Node(n, None, None)
    else:
        insert_node(tree, n)

post_order(tree)