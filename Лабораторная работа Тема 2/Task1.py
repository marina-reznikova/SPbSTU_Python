list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел

unique_numbers = set(list_)
unique_numbers_sum = sum(unique_numbers)
unique_numbers_len = len(unique_numbers)

print(unique_numbers_sum)

print(unique_numbers_len)

print(round(unique_numbers_sum / unique_numbers_len, 5))