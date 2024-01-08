import random

cpf_to_validate = ''

for i in range(9):
    cpf_to_validate += str(random.randint(0,9))

#first digit
nine_digits = cpf_to_validate
cpf_summ_1 = 0
regressive_counter = 10
for i_digit_1 in nine_digits:
    cpf_summ_1 += int(i_digit_1) * regressive_counter
    regressive_counter -= 1
digit_1_module = (cpf_summ_1 * 10) % 11
digit_1 = digit_1_module if digit_1_module <=9 else 0
# print(digit_1_module)
# print(digit_1)

#Second Digit
ten_digits = nine_digits + str(digit_1)
cpf_summ_2 = 0
regressive_counter_2 = 11

for i_digit_2 in ten_digits:
    cpf_summ_2 += int(i_digit_2) * regressive_counter_2
    regressive_counter_2 -= 1
digit_2_module = (cpf_summ_2 * 10) % 11
digit_2 = digit_2_module if digit_2_module <=9 else 0
# print(digit_2_module)
# print(digit_2)

generated_cpf_by_calc = f'{nine_digits[0:3]}.{nine_digits[3:6]}.{nine_digits[6:9]}{str("-")}{digit_1}{digit_2}'
# print(generated_cpf_by_calc)

#validating the number.

print(generated_cpf_by_calc)

  