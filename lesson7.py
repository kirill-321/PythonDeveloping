# lst1 = [23, 57, 13, 67, 75]

# result1 = sum_squares_nums(lst1)
# print(result1)


# # --------------------------

# lst2 = [14, 49, 6, 64]

# result2 = sum_squares_nums(lst2)
# print(result2)

# # --------------------------

# lst3 = [8, 90, 55, 83, 1, 22]

# new_lst3 = []

# result3 = sum_squares_nums(lst3)
# print(result3)

# # --------------------------


# def sum_squares_nums(lst):
#     new_lst = []
#     for i in lst:
#         new_lst.appen(i ** 2)
#     result = sum(new_lst)
#     return result


# import random
# import string

# def password_generation(lenPas, iSnums, isUpAlpha):
#     symbols = string.ascii_lowercase
#     password = ''
#     if isUpAlpha:
#         symbols += string.ascii_uppercase
#     if iSnums:
#         symbols += '1234567890'
#     for _ in range(lenPas):
#         password += random.choice(symbols)
#     return password

# print("---Программа для генерации пароля---")
# lenPas = int(input("Введите длину пароля: "))
# isNums = input("Нужны ли цифры в пароле? Y/N: ")
# isUpAlpha = input("Нужны ли большие буквы в пароле? Y/N: ")

# if isNums.lower() == "y":
#     isNums = True
# else:
#     isNums = False

# if isUpAlpha.lower() == "y":
#     isUpAlpha = True
# else:
#     isUpAlpha = False

# password = password_generation(lenPas, isNums, isUpAlpha)
# print(password)

# import math

# def isEven(number):
#     if number % 2 == 0:
#         return True;
#     else:
#         return False;

# if(isEven(10)):
#     print("Число 10 четное")

# def CountVowlesSymbols(text):
#     vowelsSymboys = "аеёиоуыэюя"
#     count = 0
#     for i in text: 
#         count += vowelsSymboys.count(i)

#     return count 

# def SumDigitsOfNumbers(number):
#     strNumbers = str(number)
#     summa = 0
#     for i in strNumbers:
#         summa += int(i)
#     return summa

# print(SumDigitsOfNumbers(123456789))