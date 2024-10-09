#функция определния давления
def pressure():
    f = int(input('Введите силу в Ньютонах: '))
    s = int(input('Введите площадь в м^2: '))
    print('Давление равно', round(float(f/s), 2),'Па')
pressure()