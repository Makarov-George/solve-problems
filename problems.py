#функция определния температуры
def temperature():
    T = int(input('Введите температуру в градусах Фаренгейта: '))
    print('Температура в градусах Цельсия равна', round(float((T-32)/1.8), 2),'°C')
temperature()