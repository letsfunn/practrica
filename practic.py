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



heroes = ["Жулепо Роберт", "хитрый маленький казах", "тралалела трулала", "отважный одноглазный пират шоколадных морей", "дерзкий исследователь дружеских шахт", "Dungeon Master"]
places = ["в далёком королевстве имени Мичурина", "на заброшенной фабрике старых использованных чурок", "в густом лесу кати", "на просторах лысических равнин", "у подножия гор магомеда"]
events = ["победил великого драконоборца дядю Гришу с соседнего подъезда ", "обнаружил сокровища в шкатулке усопшей бабушки", "выиграл битву со своей лудоманией", "устроил бал среди амбал", "раскрыл древнюю тайну о маленьком амулете зарытом в недрах мичурино"]
details = ["с волшебным мечом зачарованным на остроту 5 прочность 3 и отдачу 2", "на летающем ковре, который был украден на арабском базаре после того как был перекуплен у таксита которого звали хасбулла", "под звуки волшебной музыки(Подо мной м5 асфальт 8 у неё биркин цвета осень)", "с удивительной силой его бил отец в детстве (но не суть)", "в сопровождении магического существа брата дяди гриши тоже с соседнего подъезда"]


def generate_story():
    
    hero = random.choice(heroes)
    place = random.choice(places)
    event = random.choice(events)
    detail = random.choice(details)
    
   
    story = f"{hero} {place} {event} {detail}."
    return story

def save_story(story):
   
    with open("stories.txt", "a", encoding="utf-8") as file:
        file.write(story + "\n")

def main():
    while True:
        
        story = generate_story()
        print("\nСгенерированная история:")
        print(story)
        
        
        save_option = input("\nХотите сохранить эту историю в файл? (да/нет): ").lower()
        if save_option == "да":
            save_story(story)
            print("История сохранена в файл stories.txt.")
        
       
        again = input("\nХотите сгенерировать новую историю? (да/нет): ").lower()
        if again != "да":
            print("Спасибо за использование генератора историй! До свидания.")
            break


main()