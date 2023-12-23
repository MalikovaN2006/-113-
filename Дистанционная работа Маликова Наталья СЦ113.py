number = int(input("Введите номер задания:"))
if number == 1:
        s = 0
        a = 1
        print('Маликова Н СЦ113')
        print('Сумма чисел от 1 до 10')
        while a <= 10:
            s = s+a
            a = a+1
        print('Результат: ', s)
if number == 2:
    s = 0
    a = 10
    print("Сумма чисел от 10 до 50, кратные трём:")
    while a <= 50:
        
        if (a % 3) == 0:
            s = s+a 
            print(a)
        a = a+1
    
    print("Сумма всех чисел, кратные трём: ", s)
if number == 3:
    a = 3
    print("Ряд, заданных чисел:")
    while a <= 15:
        print(a)
        a = a+3
    b = 30
    while b >= 5:
        print(b)
        b = b-5
if number == 4:
    a = 1
    print("Кубы четных чисел на промежутке от 1 до 30:")
    while a <= 30:
        if (a % 2) == 0:
            print(a**3)
        a = a+1
if number == 5:
    a = 1
    s = 1
    print("Произведение чисел на промежутке от 1 до 10")
    while a <= 10:
        s = s*a
        a = a+1
    print(s)    
if number == 6:
    a = 1
    s = 1
    print("Произведение нечётных чисел на промежутке от 1 до 10")
    while a <= 10:
        if (a % 2) == 1:
            s = s*a
        a = a+1
    print(s)  
if number == 7:
    s = 0
    a = 1
    
    while a <= 50:
        if (a % 5) == 0:
            s = s+1
        a = a+1

    print("Количество чисел от 1 до 50, кратных пяти:", s)
if number == 8:
    print("Введите целое число:")
    numb = int(input())
    if (numb % 2) == 0:
        print("Число четное")
    else: 
        print("Число нечётное")
if number == 9:
    print("Введите букву латинского алфавита:")
    letter = str(input())
    letterarray = ('a', 'e', 'i', 'o', 'u')
    i = 0
    while i <= 4:
        if (letter == letterarray[i]):
            print("Введенная вами буква гласная")
            break
        elif (letter == "y"):
            print("Введенная вами буква может быть и гласной и согласной")
            break
        else:
            print("Введенная вами буква согласная")
            break
        i = i+1
if number == 10:
    cels = 1
    faren = 1
    res = 1
    print("Цельсия | Фаренгейт")
    while cels <= 100:
        if (cels % 10) == 0:
            faren = cels * 1.8 + 32
            print(cels, " | ", faren)
        cels = cels + 1
        faren = 1
if number == 11:
    print("Введите число в двоичном формате, для преобразования в десятичную:")
    dvoich = input()
    desyat = int(dvoich, 2)
    print("Двоичное число ", dvoich, " в десятичном формате: ", desyat)

