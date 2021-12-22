# # 2. Закодируйте любую строку по алгоритму Хаффмана.

# Неоптимально но самостоятельно)))

from collections import Counter, OrderedDict
from typing import Optional

from binarytree import Node, NodeValue


class MyNode(Node):

    def __init__(self, value: NodeValue, letters: str, left: Optional["Node"] = None,
                 right: Optional["Node"] = None) -> None:
        super().__init__(value, left, right)
        self.letters = letters
        self.key = None


def get_element_from_temporary_dict(key):
    value = key.replace("_", "")
    val = ord(value) if len(value) == 1 else 0
    if temporary_dict.get(key) == None:
        child_ = MyNode(val, key)
    else:
        child_ = temporary_dict.pop(key)
    return child_


def get_final_dict(node: Node, key):
    # left = 0
    # right = 1
    if node.left == None and node.right == None:
        final_dict[node.letters.replace("_", "")] = key
        return

    get_final_dict(node.left, f'{key}0')
    get_final_dict(node.right, f'{key}1')


def code_string(input_string):
    code_string = ''
    for symbol in input_string:
        code_string = code_string + final_dict.get(symbol)
    return code_string


def decode_string(code_string):
    decode_string = ''

    while len(code_string) > 0:
        for k, v in final_dict.items():
            if code_string.startswith(v):
                decode_string += k
                code_string = code_string.replace(f'{v}', '', 1)
    return decode_string

temporary_dict = {}

# input_string = input('Введите строку: ')
input_string = 'beep boop beer!'

# Строка не пустая
assert len(input_string) > 0, 'Введена пустая строка'

# Отсортированный словарь с частотами всех символов
frequency = OrderedDict(Counter(input_string))

assert len(frequency) > 1, 'строка из одного символа не поддерживается'

# Контрольная сумма вхождений
reference_weight = sum(frequency.values())

# Делать пока в словаре не останется один элемент
do_this = True

while do_this:
    # Сортирую словарь
    frequency = OrderedDict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    # Забираю два элемента с меньшим весом
    k1, v1 = frequency.popitem()
    k2, v2 = frequency.popitem()

    # и вместо них ставлю сумму их весов с ключом по конкатенации ключей
    key_for_new_elem = f'_{k1.replace("_", "")}{k2.replace("_", "")}'

    # создаю объединяющий оба значения элемент
    frequency[key_for_new_elem] = v1 + v2
    frequency.move_to_end(key_for_new_elem, last=False)

    # Для каждого элемента делаю или нахожу уже существующий лист
    child_1 = get_element_from_temporary_dict(f'_{k1.replace("_", "")}')
    child_2 = get_element_from_temporary_dict(f'_{k2.replace("_", "")}')

    # Новый, объединяющий узел создаю и помещаю в temporary_dict
    parent = get_element_from_temporary_dict(key_for_new_elem)
    parent.left = child_1
    parent.right = child_2

    temporary_dict[key_for_new_elem] = parent

    # Если список сократился до одного элемента, прекращаем
    do_this = len(frequency) > 1
    if not do_this:
        break

# Посмотрим на дерево
for value in temporary_dict.values():
    print(value)

# Заполню словарь преобразования
final_dict = {}
get_final_dict(temporary_dict.popitem()[1], '')

print(final_dict)
assert reference_weight == sum(frequency.values()), 'Ошибка вычисления контрольной суммы вхождений'

code_string = code_string(input_string)

print('Кодированная строка:', code_string)

print('Декодированная строка:', decode_string(code_string))
