print ("Камень -"("1"))
print ("Ножницы - 2")
print ("Бумага - 3")
a = int(input("Сделай свой выбор номер 1 -"))
d == int(input("Сделай выбор номер 2 -"))
if a == "1" and d == "1":
    print("Ничья")
elif a =="1" and d == "2":
    print("Вы выйграли")
elif a =="1" and d == "3":
    print("Вы выпроиграли")
elif a == "2" and d =="2":
    print("Ничья")
elif a == "2" and d == "1":
    print("Вы проиграли")
elif a ==  "2" and d == "3":
    print("Вы выйграли")
elif a == "2" and d == "3":
    print("Вы выйграли")
elif a == "3" and d == "1":
    print("Вы выйграли")
elif a == "3" and d == "3":
    print("Ничья")
elif a == "3" and d == "2":
    print("Вы выпроиграли")

