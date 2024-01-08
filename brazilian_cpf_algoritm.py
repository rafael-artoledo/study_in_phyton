"""
The brazilian goverment has an algoritm to validate the brazilian social security number(CPF),
and here I will make the algoritm work.
"""
# I did it before teacher´s solve class part 1, 
# I admit, I didn´t remebered the teacher´s classes that could simplify a lot the code.

# import os
# i=0
# numbers='0123456789'
# while True:
#     cpf_entry = input('CPF: ')
#     if len(cpf_entry) >14 or len(cpf_entry) <14 :
#         os.system('cls')
#         print('Press just numbers as example: "888.888.888-88"')
#         continue
    
#     cpf_to_validate= ''
#     for i in cpf_entry:
        
#         if i in numbers:
#             cpf_to_validate += i
#         else:
#             pass
#     if  len(cpf_to_validate) <11 or len(cpf_to_validate) > 11:
#         os.system('cls')
#         print('The CPF number must have 11 numbers with the especial symbols "." and "-",' 
#               ' a total of 14 symbols: "888.888.888-88".')
#         continue


#     
#     cpf_vali_int = []
#     for i in cpf_to_validate:
#         cpf_vali_int.append(int(i))
#    
#     cpf_summ = (cpf_vali_int[0]*10 + cpf_vali_int[1]*9 + cpf_vali_int[2]*8 + cpf_vali_int[3]*7 
#     + cpf_vali_int[4]*6 + cpf_vali_int[5]*5 + cpf_vali_int[6]*4 + cpf_vali_int[7]*3 
#     + cpf_vali_int[8]*2)
#     print(cpf_summ)
#     digit_1_module = (cpf_summ * 10) % 11
#################################################################################################
import os
import re
import sys
cpf_entry = input('CPF: ')

cpf_to_validate = re.sub( r'[^0-9]', '', cpf_entry)

sequencial_entry = cpf_entry == cpf_entry[0]*len(cpf_entry)

if sequencial_entry:
    print('You entered sequencial data.')
    sys.exit()
#first digit
nine_digits = cpf_to_validate[:9]
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
ten_digits = cpf_to_validate[:10]
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
if generated_cpf_by_calc == cpf_entry:
    print(f'{generated_cpf_by_calc} is valid.')
else:
    print('CPF is not valid.')

    # teacher way first digit
    #
    # cpf='74682489070'
    # nine_digits = cpf[:9]
    # regressive_counter = 10
    # result = 0
    # for digit in nine_digits:
    #    result = int(digit)* regressive_counter
    #    regressive_counter -= 1
    # digit_1 = digit_1 if digit <=9 else 0   
