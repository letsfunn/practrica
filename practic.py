import random
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



# heroes = ["Жулепо Роберт", "хитрый маленький казах", "тралалела трулала", "отважный одноглазный пират шоколадных морей", "дерзкий исследователь дружеских шахт", "Dungeon Master"]
# places = ["в далёком королевстве имени Мичурина", "на заброшенной фабрике старых использованных чурок", "в густом лесу кати", "на просторах лысических равнин", "у подножия гор магомеда"]
# events = ["победил великого драконоборца дядю Гришу с соседнего подъезда ", "обнаружил сокровища в шкатулке усопшей бабушки", "выиграл битву со своей лудоманией", "устроил бал среди амбал", "раскрыл древнюю тайну о маленьком амулете зарытом в недрах мичурино"]
# details = ["с волшебным мечом зачарованным на остроту 5 прочность 3 и отдачу 2", "на летающем ковре, который был украден на арабском базаре после того как был перекуплен у таксита которого звали хасбулла", "под звуки волшебной музыки(Подо мной м5 асфальт 8 у неё биркин цвета осень)", "с удивительной силой его бил отец в детстве (но не суть)", "в сопровождении магического существа брата дяди гриши тоже с соседнего подъезда"]


# def generate_story():
    
#     hero = random.choice(heroes)
#     place = random.choice(places)
#     event = random.choice(events)
#     detail = random.choice(details)
    
   
#     story = f"{hero} {place} {event} {detail}."
#     return story

# def save_story(story):
   
#     with open("stories.txt", "a", encoding="utf-8") as file:
#         file.write(story + "\n")

# def main():
#     while True:
        
#         story = generate_story()
#         print("\nСгенерированная история:")
#         print(story)
        
        
#         save_option = input("\nХотите сохранить эту историю в файл? (да/нет): ").lower()
#         if save_option == "да":
#             save_story(story)
#             print("История сохранена в файл stories.txt.")
        
       
#         again = input("\nХотите сгенерировать новую историю? (да/нет): ").lower()
#         if again != "да":
#             print("Спасибо за использование генератора историй! До свидания.")
#             break


# main()



# def print_field(field):
#     print()
#     print(f" {field[0]} | {field[1]} | {field[2]}")
#     print("-----------")
#     print(f" {field[3]} | {field[4]} | {field[5]}")
#     print("-----------")
#     print(f" {field[6]} | {field[7]} | {field[8]}")
#     print()

# def check_win(field, symbol):
#     win_combinations = [
#         (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
#         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
#         (0, 4, 8), (2, 4, 6)              # диагонали
#     ]
#     for combo in win_combinations:
#         if field[combo[0]] == field[combo[1]] == field[combo[2]] == symbol:
#             return True
#     return False

# def play_game():
#     while True:
#         field = [str(i) for i in range(1, 10)]
#         current_player = 'X'
#         moves = 0

#         while True:
#             print_field(field)

#             try:
#                 move = int(input(f"Игрок {current_player}, выберите клетку (1-9): "))
#                 if move < 1 or move > 9:
#                     print("Ошибка: введите число от 1 до 9.")
#                     continue
#                 if field[move - 1] in ['X', 'O']:
#                     print("Ошибка: клетка уже занята.")
#                     continue
#             except ValueError:
#                 print("Ошибка: введите корректное число.")
#                 continue

#             field[move - 1] = current_player
#             moves += 1

#             if check_win(field, current_player):
#                 print_field(field)
#                 print(f"Поздравляем! Игрок {current_player} победил!")
#                 break

#             if moves == 9:
#                 print_field(field)
#                 print("Ничья!")
#                 break

#             current_player = 'O' if current_player == 'X' else 'X'

#         again = input("Сыграть ещё раз? (Y/N): ").strip().upper()
#         if again != 'Y':
#             print("Спасибо за игру!")
#             break

# # Запуск игры
# play_game()
