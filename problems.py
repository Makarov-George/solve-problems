#функция определния потенциальной энергии
def potencial_energy():
    m = int(input('Введите массу в килограммах: '))
    h = int(input('Введите высоту в метрах: '))
    g = int(input('Введите ускорение свободного падения: '))
    print('Потенциальная энергия равна', round(float(m*g*h), 2),'Дж')
potencial_energy()