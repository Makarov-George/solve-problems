#функция определния частоты
def frequency():
    t = int(input('Введите период колебаний в секунду: '))
    print('Частота равна', round(float(1/t), 2),'Гц')
frequency()