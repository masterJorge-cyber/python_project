# x_total = 0

# def soma(x):
#     global x_total
#     x_total += int(x)
#     print(f"Soma atual: {x_total}")

# print("Digite um valor para soma, e -1 para sair:")

# while True:
#     x = int(input())
#     if x == -1:
#         break
#     soma(x)


def soma(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(f"Soma: {total}")


soma(1, 2, 3, 4)   # Soma: 10
soma(5, 10)        # Soma: 15
