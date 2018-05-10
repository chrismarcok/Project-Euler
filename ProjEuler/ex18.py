from typing import Union

def get_num(s: str) -> int:
    """
    >>> get_num("02")
    2
    >>> get_num("00")
    0
    >>> get_num("12")
    12
    """
    if s == "00":
        return 0
    elif s[0] == '0':
        return int(s[1])
    else:
        return int(s)

file = open("triangle67.txt", "r")
data = file.read()
data = data.split("\n")
for x in range(len(data)):
    data[x] = data[x].split(" ")
for sublist in data:
    for x in range(len(sublist)):
        sublist[x] = get_num(sublist[x])

"""
now we have traingle:
   3
  7 4
 2 4 6
8 5 9 3

equals
[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
"""
class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    value: int
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, value: int,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        self.value, self.left, self.right = value, left, right


def populate_tree(data: list, depth: int = 0, rightness: int = 0) -> Union[BTNode, None]:
    if depth >= len(data) or rightness >= len(data):
        return None
    return BTNode(data[depth][rightness],
           populate_tree(data, depth + 1, rightness),
           populate_tree(data, depth + 1, rightness + 1))


tree = populate_tree(data)

def max_distance(node: BTNode) -> int: # bruteforce the max path
    if node is None:
        return 0
    else:
        if max_distance(node.left) > max_distance(node.right):
            return node.value + max_distance(node.left)
        else:
            return node.value + max_distance(node.right)

print(max_distance(tree))
