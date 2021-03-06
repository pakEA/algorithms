"""
Закодировать любую строку по алгоритму Хаффмана.
"""
from collections import Counter, deque


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):
    count_str = Counter(s)
    sorted_str = deque(sorted(count_str.items(), key=lambda item: item[1]))
    while len(sorted_str) > 1:
        weight = sorted_str[0][1] + sorted_str[1][1]
        node = MyNode(left=sorted_str.popleft()[0], right=sorted_str.popleft()[0])
        for i, item in enumerate(sorted_str):
            if weight > item[1]:
                continue
            else:
                sorted_str.insert(i, (node, weight))
                break
        else:
            sorted_str.append((node, weight))

    return sorted_str[0][0]


code_dict = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, MyNode):
        code_dict[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


user_string = "beep boop beer!"

haffman_code(haffman_tree(user_string))

for letter in user_string:
    print(f'Код символа {letter}: {code_dict[letter]}', end='\n')
