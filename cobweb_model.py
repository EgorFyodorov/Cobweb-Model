import matplotlib.pyplot as plt

print('Qd = a - b*P')
print('Qs = c + d*P')
print('Введите a, b, c, d:')
a, b, c, d = map(float, input().split())
try:
	p_balance = (a - c)/(d + b)
	q_balance = a - b * p_balance
	print('P* =', p_balance)
	print('Q* =', q_balance)
except:
	print('Невозможно определить равновесные цену и объём')

price_calculation = lambda q: (a - q)/b #цена определяется спросом 
quantuty_calculation = lambda p: c + d * p #объём определяется предложением

p, q = [], []

k = 5 #точность при потенциально нестабильном рынке
h = 25 #точность при потенциально стабильном рынке

if d > b:
	print('Отклонение от равновесных параметров будет только увеличиваться')
elif d == b:
	print('Рыночная цена будет то и делать, что циклически колебаться')
else:
	print('Рынок будет приближаться к состоянию равновесия')

print("Введите начальный объём:")
q.append(int(input('Q1 = ')))
p.append(price_calculation(q[0]))

print('Введите точность последующих вычислений:')
print('(Количество высчитываемых единиц)')
k = int(input())

for i in range(1, k, 2):
	q_new = quantuty_calculation(p[i - 1])
	p_new = price_calculation(q_new)
	q += [q_new, q_new]
	p += [p[i - 1], p_new]

for i in range(0, k, 2):
	print('Q', end = '')
	print(i//2 + 1,'=', q[i])
	print('P', end = '')
	print(i//2 + 1,'=', p[i])
	
#Начинаем рисовать  Q P
plt.figure(figsize=(12, 7))

plt.subplot(1, 2, 1)
plt.title('Поле рыночного обмена', fontsize=15)
plt.grid()
plt.xlabel('Q')
plt.ylabel('P')
plt.plot([a, q_balance, 0], [0, p_balance, a/b], c = 'b', label = 'Кривая спроса', lw = 2) #кривая спроса
plt.plot([c, q_balance, c + d*a/b], [0, p_balance, a/b], c = 'r', label = 'Кривая предложения', lw = 2) #кривая предложения
plt.plot(q, p, 'D-k', label = 'Динамика равновесия', lw = 1, ms = 3)
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Динамика цены', fontsize=15)
plt.grid()
plt.xlabel('T')
plt.ylabel('P')
plt.plot(p[0:k:2], '.-k', lw = 2, label = 'Фактическая цена') #динамика цены
plt.plot([p_balance for i in range(k//2 + 1)], ',-.b', lw = 1, label = 'Равновесная цена') #стационарная прямая равновесной цены
plt.legend()

plt.show() 