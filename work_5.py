import numpy as np
import scipy.stats as stats


# Задача 1. Когда используется критерий Стьюдента, а когда Z –критерий?
# Критерий Стьюдента изпользуется если генеральная совокупность неизвестна, так же при двухвыборочном тесте,
# при неизвестной дисперсии генеральной совокупности, а так же при нормальном распределении.

# Z-критерий выбираем когда тест одновыборочный, известна дисперсия генеральной совокупности и 
# при нормальном распределении.
###########################################################################################
###########################################################################################

# Задача 2. Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные
# автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из
# n=100 шариков средний диаметр
# оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.

# Формулирование гипотез
# Ho = M = Mo
# H1 = M > Mo

# # Статистическая значимость задана, а = 1,65
# a = 0.05

# # Будем использовать Z-критерий, так как тест одновыборочный, известна дисперсия генеральной
# # совокупности.

# z= (17.5-17)/(16/np.sqrt(100))
# print(z)
# Z расчётная 0,3125 меньше Z табличной 1,65 по этому мы не отвергаем Но.

###################################################################################################
###################################################################################################

# Задача 3. Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
# составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна
# 99%? (Провести двусторонний тест.)
# a = 0.01
# m0 = 200
# n = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
# m = np.mean(n)
# print(m)
# s = np.var(n)
# print(s)

# t = (m-m0)/(s/np.sqrt(10))
# print(t)
# # По таблице критических точек распределения Стьюдента найдем критическую точку по
# # уровню значимости α = 0,01 и числу степеней свободы k = 9 , откуда t_k = 3,25
# t_1 = 3.25
# a_1 = t_1/2
# print(a_1)
# Т расчётная не попадает в критическую область -1,625 < -0.26 < 1.625 . Гипотеза 0 не отвергается.

####################################################################################
####################################################################################

# Задача 4. Есть ли статистически значимые различия в росте дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163

x = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
x_m = np.mean(x)
y_m = np.mean(y)
x_n = len(x)
y_n = len(y)
x_v = np.var(x, ddof=1)
y_v = np.var(y, ddof=1)

t_r = (x_m-y_m)/ np.sqrt(x_v/x_n + y_v/y_n)
print(t_r)

alpha = 0.05
n = 200
t = stats.t.ppf(alpha/2, 2*(n-1))
t_1 = stats.t.ppf(1-alpha/2, 2*(n-1))
print(t)
print(t_1)
# Т расчётная не попадает в критическую область -1,96 < 0.41 < 1.96 . Гипотеза 0 не отвергается.

tt = stats.ttest_ind(x,y)
print(tt)

# pvalue > alpha нулевая гипотеза не отвергается







