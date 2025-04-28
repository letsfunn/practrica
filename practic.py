# import random
# def game():
#     number = random.randint(1,100)
#     trai = 0
#     while True:
#         try:
#             player_num = int(input("Введите число: "))
#             trai += 1
#             if player_num < number:
#                 print("Число больше")
#             elif player_num > number:
#                 print("Число меньше")
#             else:
#                 print(f"Победа, загаданное число было {number} Попыток {trai}")
#                 break
#         except ValueError:
#             print("Пожалуйста, введите целое число.")


# def main():
#    while True:
#         game()
#         play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
#         if play_again != 'да':
#             print("Спасибо за игру!")
#             break

# main()