n = int(input('Какое количество замеров (n) вы имеете?: '))

arr = []

arr.append(float(input('Что взять за X0? - ')))

for i in range(1, n):
    arr.append(float(input(f'Введите {i+1}ое число: ')))

errs = []

# Xi - X0
for i in range(n):
    errs.append(arr[i] - arr[0])

#Среднее значение
midX = arr[0] + ((1/n)*(sum(errs)))
print(f'Среднее значение: {midX}')

#Среднеквадратичная погрешность

#(xi-x0)^2-n(x-x0)^2

helpFormulas = []

for i in range(n):
    helpFormulas.append((arr[i] - arr[0])**2 - (n*(midX - arr[0])**2))

RMSf = abs((1/(n*(n-1)))*(sum(helpFormulas)))
print(f'Среднеквадратичная погрешность: {RMSf}')

#Стандартное отклонение
standErr = RMSf ** (0.5)
print(f'Стандартное отклонение: {standErr}')

#Коэффициент Стьюдента (alpha = 0,95)
coeff = [12.7060, 4.3020, 3.182, 2.776, 2.570, 2.4460, 2.3646, 2.3060, 2.2622, 2.2281]

#Абсолютная погрешность
ABSerr = coeff[n - 1] * standErr
print(f'Абсолютная погрешность: {ABSerr}')

#Относительная погрешность

otnErr = (ABSerr / midX) * 100
print(f'Относительная погрешность: {otnErr}')



