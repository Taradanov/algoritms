# import random
#
# import item as item
#
#
# def one():
#     array =[random.randint(-100, 100) for i in range(100000)]
#     arr_below = []
#     arr_lager = []
#
#     for item in array:
#         if item >= 0:
#             arr_lager.append(item)
#         else:
#             arr_below.append(item)
#
#
# def two():
#     array = [random.randint(-100, 100) for i in range(1000000)]
#     arr_below = [item for item in array if item < 0]
#     arr_lager = [item for item in array if item > 0]
#
# one()
# two()
import random
from pprint import pprint

matrix = [[random.randint(1, 10) for i in range(5)] for i in range(7)]
pprint(matrix)
