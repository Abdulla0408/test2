# VAZIFALAR
# 1.
# meal = ['Osh', 'Shorva', 'Shashlik']
# meal.append('Osh')
# meal.append('Shorva')
# meal.insert(2, 'Shashlik')
# meal.insert(4,'Hot Dog')
# print(tuple(meal))

# ----------------------------------------------------------------------------------------------------------------------------

# 2.
# letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
# lowercase_letter = []
# capital_letter = []
# for i in letters:
#     if i.isupper():
#         capital_letter.append(i)
#     elif i.islower():
#         lowercase_letter.append(i)
# #
# print(tuple(capital_letter))
# print(tuple(lowercase_letter))

# ----------------------------------------------------------------------------------------------------------------------------

# 3.
# name = ['Akmal', 'abror', 'toxir', 'Sobir', 'Bakir', 'jalil']
# capital_letter = []
# lowercase_letter = []
# for i in name:
#     if i.istitle():
#         capital_letter.append(i)
#     elif i.islower():
#         lowercase_letter.append(i)
#
# print(tuple(capital_letter))
# print(tuple(lowercase_letter))

# ----------------------------------------------------------------------------------------------------------------------------

# 4.
# numbers = ['+998901234567','+79454874459', '+14385001031']
# uzb_num = []
# rus_num = []
# us_num = []
# def number(p_numbers):
#     for i in p_numbers:
#         if i.startswith('+998'):
#             uzb_num.append(i)
#         elif i.startswith('+7'):
#             rus_num.append(i)
#         elif i.startswith('+1'):
#             us_num.append(i)
# number(numbers)
# print(uzb_num)
# print(rus_num)
# print(us_num)

# ----------------------------------------------------------------------------------------------------------------------------

# 5.
# n = int(input('N sonini kiriting: '))
# toq_son = []
# if n > 0:
#     for i in range(0,n):
#         if i % 2 != 0:
#             toq_son.append(i)
# print(toq_son)

# ----------------------------------------------------------------------------------------------------------------------------

# 6.
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399,
# 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
# 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
# numbers.sort()
# sort_num = []
# for i in numbers:
#     sort_num.append(i)
#     if i == 815:
#         break
# print(sort_num)

# ----------------------------------------------------------------------------------------------------------------------------

# 8.
# d = {'a': 1, 'b': 2, 'c': 3}
# yigindi = 0
# for i in d.values():
#     yigindi = yigindi + i

# print(f'Lugatning qiymatlari yigindisi: {yigindi} ga teng')

# ----------------------------------------------------------------------------------------------------------------------------

# 9.
# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# yigindi = 0
# for i in d.keys():
#     yigindi = yigindi + i

# print(f'Lugatning kalitlari yigindisi: {yigindi} ga teng')

# ----------------------------------------------------------------------------------------------------------------------------

# 11.
d = {'a': 1, 'b': 2, 'c': 3}
yigindi = 0
count = 0
for i in d.values():
    count = count + 1
    yigindi = yigindi + i

print(f'Lugatning qiymatlari orta arfimetigi: {yigindi/count} ga teng')

# ----------------------------------------------------------------------------------------------------------------------------

student = {
    'name': 'Abdulla',
    'age': 15,
    'class': 9
}
print(student.items())
