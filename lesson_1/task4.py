n = int(input())


change_type = input() # b или k

if change_type == 'b':
    print(f'{n*1024} байтов')
elif change_type == 'k':
    print(f'{n/1024} Килобайтов')