
color_red = "Красный"
color_yellow = "Желтый"
color_green = "Зеленый"  
print(color_red, color_yellow, color_green)
print("Выберите цвет")
user_c = input("Твой цвет")
if user_c == "Красный":
    print("Стой")
elif user_c == "Желтый" or "Зеленый":
    print("Подожди и иди")
else:
    print("Error")         