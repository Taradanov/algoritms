# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict, Counter, OrderedDict
from pprint import pprint

company = defaultdict(list)

def add_company(name, fm, sm, tm, ft):
    company[name].append(fm)
    company[name].append(sm)
    company[name].append(tm)
    company[name].append(ft)


# Добавил организации
add_company('company_1', 110_000, 90_000, 100_000, 80_000)
add_company('company_2', 10_000, 9_000, 100_000, 80_000)
add_company('company_3', 110_000, 90_000, 10_000, 8_000)
add_company('company_4', 110_000, 9_000, 1_000, 80_000)
add_company('company_5', 900_000, 100_000, 100_000, 1_00_000)
add_company('company_6', 0, 0, 0, 0)
add_company('company_7', 0, 0, 400_000, 0)

pprint(company)

# Средне квартальная прибыль
average_monthly = Counter()

for key, value in company.items():
    average_monthly[key] = sum(value) / 4

pprint(average_monthly)

# Средняя по всем предприятиям
average_cost = sum([average_monthly[v] for v in average_monthly]) / len(average_monthly)
print('Средняя по всем предприятиям:', average_cost)

# Сформирую сортированные по наименованию словари предприятий
less_than_average = OrderedDict({key: value for key, value in average_monthly.items() if value <= average_cost})
more_than_average = OrderedDict({key: value for key, value in average_monthly.items() if value > average_cost})

print('Меньше среднего:')
pprint(less_than_average)
print('Больше среднего:')
pprint(more_than_average)
