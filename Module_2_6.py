import random


def secret():
    draft = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    number = random.choice(draft)
    return number


number = secret()
print('Секрет: ')

print(number)
print('Введите секретный код:')


def password(numbers):
    result = ''
    for i in range(1, numbers):
        for j in range(i + 1, numbers):
            if numbers % (i + j) == 0:
                result += str(i) + str(j)
    return result



print('Секретный пароль:', password(int(input())))

