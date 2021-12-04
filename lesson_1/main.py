



def main(n, change_type):
    if change_type == 'b':
        return(f'{n*1024} байтов')
    elif change_type == 'k':
        return(f'{n/1024} Килобайтов')


# синтаксис
#assert <проверяемое утверждение>, <сообщение об ошибке>


def test():
    n = 1024 # байт
    change_type = 'k'
    assert main(n, change_type) == '1.0 Килобайтов'

    n = 1 # кбайт
    change_type = 'b'
    assert main(n, change_type) == '1024 байтов'

    print('DONE')


test()