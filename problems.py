#функция определния массы
def mass():
    f = int(input('Введите силу в Ньютонах: '))
    a = int(input('Введите ускорение в м/(с^2): '))
    print('Масса равна', round(float(f/a), 2),'кг')
mass()