"""
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных
 числа X и Y (X,Y≤1000), а Катя должна их отгадать.
 Для этого Петя делает две подсказки.
 Он называет сумму этих чисел S и их произведение P.
 Помогите Кате отгадать задуманные Петей числа.
"""

S, P = map(float, input("Введите значения суммы и произведения загаданных чисел через запятую: ").split(","))
d = S**2-4*P
x = round((S+d**0.5)//2)
y = round((S-d**0.5)//2)

print(x, y)
