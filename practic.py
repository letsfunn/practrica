import random
import pygame
import sys
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


# class Character:
#     def __init__(self, name, health, attack, defence):
#         self.name = name
#         self.health = health
#         self.attack = attack
#         self.defence = defence

#     def attack_target(self, other):
#         damage = max(self.attack - other.defence, 0)
#         other.health -= damage
#         print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

# def print_status(hero, monster):
#     print("\n--- Состояние персонажей ---")
#     print(f"{hero.name}: Здоровье = {hero.health}, Атака = {hero.attack}, Защита = {hero.defence}")
#     print(f"{monster.name}: Здоровье = {monster.health}, Атака = {monster.attack}, Защита = {monster.defence}")
#     print("-----------------------------\n")

# def battle():
#     while True:
#         hero = Character("Герой", 100, 20, 5)
#         monster = Character("Монстр", 80, 15, 3)

#         while hero.health > 0 and monster.health > 0:
#             print_status(hero, monster)

#             # Ход игрока
#             while True:
#                 print("Выберите действие:")
#                 print("0 - Атака")
#                 print("1 - Пропустить ход")
#                 choice = input("Ваш выбор: ")
#                 if choice not in ['0', '1']:
#                     print("Ошибка: выберите 0 или 1.")
#                 else:
#                     break

#             if choice == '0':
#                 hero.attack_target(monster)
#             else:
#                 print(f"{hero.name} пропускает ход.")

#             if monster.health <= 0:
#                 print(f"{monster.name} побежден! Вы выиграли!")
#                 break

#             # Ход монстра
#             monster_choice = random.choice(['attack', 'skip'])
#             if monster_choice == 'attack':
#                 monster.attack_target(hero)
#             else:
#                 print(f"{monster.name} пропускает ход.")

#             if hero.health <= 0:
#                 print(f"{hero.name} побежден! Вы проиграли!")
#                 break

#         again = input("Сыграть снова? (Y/N): ").strip().upper()
#         if again != 'Y':
#             print("Спасибо за игру!")
#             break

# # Запуск игры
# battle()

# class Player:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.health = 100

#     def move(self, direction, field_size):
#         dx, dy = 0, 0
#         if direction == 'w':
#             dx = -1
#         elif direction == 's':
#             dx = 1
#         elif direction == 'a':
#             dy = -1
#         elif direction == 'd':
#             dy = 1

#         new_x = self.x + dx
#         new_y = self.y + dy

#         if 0 <= new_x < field_size and 0 <= new_y < field_size:
#             self.x = new_x
#             self.y = new_y
#             return True
#         else:
#             print("Нельзя выйти за пределы поля!")
#             return False

# def generate_field(size, player):
#     field = [['.' for _ in range(size)] for _ in range(size)]

#     # Размещаем ловушки
#     num_traps = random.randint(3, 5)
#     traps = set()
#     while len(traps) < num_traps:
#         x, y = random.randint(0, size-1), random.randint(0, size-1)
#         if (x, y) != (0, 0):
#             traps.add((x, y))
#     for x, y in traps:
#         field[x][y] = 'T'

#     # Размещаем выход
#     while True:
#         x, y = random.randint(0, size-1), random.randint(0, size-1)
#         if (x, y) != (0, 0) and field[x][y] != 'T':
#             field[x][y] = 'X'
#             break

#     return field

# def print_field(field, player):
#     size = len(field)
#     for i in range(size):
#         row = ''
#         for j in range(size):
#             if (i, j) == (player.x, player.y):
#                 row += 'P '
#             else:
#                 row += field[i][j] + ' '
#         print(row.strip())
#     print(f"\nЗдоровье игрока: {player.health}\n")

# def game():
#     while True:
#         size = 5
#         player = Player()
#         field = generate_field(size, player)

#         while True:
#             print_field(field, player)

#             direction = input("Введите направление (w/a/s/d): ").strip().lower()
#             if direction not in ['w', 'a', 's', 'd']:
#                 print("Ошибка: введите одну из клавиш w/a/s/d.")
#                 continue

#             moved = player.move(direction, size)
#             if not moved:
#                 continue

#             current_cell = field[player.x][player.y]
#             if current_cell == 'T':
#                 player.health -= 20
#                 print("Вы наступили на ловушку! -20 HP")
#                 field[player.x][player.y] = '.'
#             elif current_cell == 'X':
#                 print_field(field, player)
#                 print("Поздравляем! Вы нашли выход и победили!")
#                 break

#             if player.health <= 0:
#                 print_field(field, player)
#                 print("Вы проиграли! Здоровье закончилось.")
#                 break

#         again = input("Хотите сыграть снова? (Y/N): ").strip().upper()
#         if again != 'Y':
#             print("Спасибо за игру!")
#             break

# # Запуск игры
# game()


# --- Инициализация ---
# pygame.init()
# WIDTH, HEIGHT = 600, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Камень, Ножницы, Бумага!")
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 36)

# # --- Цвета ---
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)
# BLUE = (100, 100, 255)

# # --- Переменные состояния ---
# choices = ['Камень', 'Бумага', 'Ножницы']
# player_choice = None
# computer_choice = None
# result = None
# game_active = True

# # --- Кнопки ---
# button_width, button_height = 150, 50
# buttons = {
#     'Камень': pygame.Rect(75, 150, button_width, button_height),
#     'Бумага': pygame.Rect(225, 150, button_width, button_height),
#     'Ножницы': pygame.Rect(375, 150, button_width, button_height)
# }

# # --- Логика определения победителя ---
# def determine_winner(player, computer):
#     if player == computer:
#         return "Ничья!"
#     elif (player == "Камень" and computer == "Ножницы") or \
#          (player == "Ножницы" and computer == "Бумага") or \
#          (player == "Бумага" and computer == "Камень"):
#         return "Вы выиграли!"
#     else:
#         return "Вы проиграли!"

# # --- Отрисовка текста ---
# def draw_text(text, x, y, center=True, color=BLACK):
#     rendered = font.render(text, True, color)
#     rect = rendered.get_rect()
#     if center:
#         rect.center = (x, y)
#     else:
#         rect.topleft = (x, y)
#     screen.blit(rendered, rect)

# # --- Основной игровой цикл ---
# running = True
# while running:
#     screen.fill(WHITE)

#     draw_text("Камень Ножницы Бумага!", WIDTH // 2, 40)
#     draw_text("Выберите свой ход (клавиши R, P, S или нажмите кнопку)", WIDTH // 2, 70, color=BLUE)

#     # Рисуем кнопки
#     for name, rect in buttons.items():
#         pygame.draw.rect(screen, GRAY, rect)
#         draw_text(f"{name} ({name[0]})", rect.centerx, rect.centery)

#     # Отображение выбора и результата
#     if player_choice and computer_choice:
#         draw_text(f"Вы выбрали: {player_choice}", WIDTH // 2, 250)
#         draw_text(f"Компьютер выбрал: {computer_choice}", WIDTH // 2, 280)
#         draw_text(result, WIDTH // 2, 320, color=(0, 150, 0))
#         draw_text("Нажмите ПРОБЕЛ чтобы сыграть снова", WIDTH // 2, 360, color=BLUE)
#     else:
#         draw_text("Сделайте свой выбор!", WIDTH // 2, 360, color=BLUE)

#     # --- Обработка событий ---
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         elif event.type == pygame.KEYDOWN and game_active:
#             if event.key == pygame.K_r:
#                 player_choice = "Камень"
#             elif event.key == pygame.K_p:
#                 player_choice = "Бумага"
#             elif event.key == pygame.K_s:
#                 player_choice = "Ножницы"

#             if player_choice:
#                 computer_choice = random.choice(choices)
#                 result = determine_winner(player_choice, computer_choice)
#                 game_active = False

#         elif event.type == pygame.MOUSEBUTTONDOWN and game_active:
#             if event.button == 1:
#                 for name, rect in buttons.items():
#                     if rect.collidepoint(event.pos):
#                         player_choice = name
#                         computer_choice = random.choice(choices)
#                         result = determine_winner(player_choice, computer_choice)
#                         game_active = False

#         elif event.type == pygame.KEYDOWN and not game_active:
#             if event.key == pygame.K_SPACE:
#                 player_choice = None
#                 computer_choice = None
#                 result = None
#                 game_active = True

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.exit()


# --- Настройка Pygame ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Поймай Призрака!")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- Цвета ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Настройки игры ---
GHOST_SIZE = 80
GAME_DURATION = 30_000  # 30 секунд
GHOST_LIFE = 700        # Призрак "живёт" 0.7 секунды
SPAWN_MIN = 1000
SPAWN_MAX = 2000

# --- Загрузка изображения призрака ---
ghost_img = pygame.Surface((GHOST_SIZE, GHOST_SIZE), pygame.SRCALPHA)
pygame.draw.circle(ghost_img, (200, 200, 255, 180), (GHOST_SIZE//2, GHOST_SIZE//2), GHOST_SIZE//2)

# --- Звук (опционально) ---
# catch_sound = pygame.mixer.Sound("catch.wav")  # если нужен звук

# --- Состояние ---
score = 0
start_time = 0
game_over = False
ghost_rect = pygame.Rect(-100, -100, GHOST_SIZE, GHOST_SIZE)
ghost_visible = False
ghost_spawn_time = 0
ghost_hide_time = 0

# --- Генерация нового призрака ---
def spawn_ghost():
    x = random.randint(0, WIDTH - GHOST_SIZE)
    y = random.randint(100, HEIGHT - GHOST_SIZE)
    return pygame.Rect(x, y, GHOST_SIZE, GHOST_SIZE)

# --- Основной игровой цикл ---
def reset_game():
    global score, start_time, game_over, ghost_visible, ghost_rect
    global ghost_spawn_time, ghost_hide_time

    score = 0
    start_time = pygame.time.get_ticks()
    game_over = False
    ghost_visible = False
    ghost_spawn_time = start_time + random.randint(SPAWN_MIN, SPAWN_MAX)
    ghost_hide_time = 0
    ghost_rect = pygame.Rect(-100, -100, GHOST_SIZE, GHOST_SIZE)

reset_game()

running = True
while running:
    current_time = pygame.time.get_ticks()
    elapsed = current_time - start_time
    remaining = max(0, (GAME_DURATION - elapsed) // 1000)

    screen.fill(WHITE)

    # Заголовок и UI
    text = font.render("Поймай Призрака!", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

    score_text = font.render(f"Счёт: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    time_text = font.render(f"Время: {remaining}", True, BLACK)
    screen.blit(time_text, (WIDTH - 150, 20))

    hint_text = font.render("Кликай по призраку, пока не закончится время!", True, BLACK)
    screen.blit(hint_text, (WIDTH // 2 - hint_text.get_width() // 2, 60))

    # Показываем призрака
    if not game_over and ghost_visible:
        screen.blit(ghost_img, ghost_rect.topleft)

    # Проверка окончания игры
    if elapsed >= GAME_DURATION and not game_over:
        game_over = True
        ghost_visible = False

    if game_over:
        over_text = font.render(f"Время вышло! Ваш счёт: {score}", True, BLACK)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 20))

        restart_text = font.render("Нажмите ПРОБЕЛ, чтобы начать заново", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ghost_visible:
            if ghost_rect.collidepoint(event.pos):
                score += 1
                ghost_visible = False
                # catch_sound.play()

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                reset_game()

    # Обновление состояния призрака
    if not game_over:
        if ghost_visible and current_time >= ghost_hide_time:
            ghost_visible = False
            ghost_spawn_time = current_time + random.randint(SPAWN_MIN, SPAWN_MAX)
        elif not ghost_visible and current_time >= ghost_spawn_time:
            ghost_rect = spawn_ghost()
            ghost_visible = True
            ghost_hide_time = current_time + GHOST_LIFE

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()




