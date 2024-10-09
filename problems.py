#функция определния кинетической энергии
def kinetic_energy():
    m = int(input('Введите массу в килограммах: '))
    v = int(input('Введите скорость в м/с: '))
    print('Кинетическая энергия равна', round(float((m*v*v)/2), 2),'Дж')
kinetic_energy()