# task 1
num = int(input("Enter a four-digit num: "))
if num < 1000 or num > 9999:
    print("Error: this num is not four-digit!")
else:
    str_num = str(num)
    digits_of_num = list(str_num)
    sum_of_first_half = int(digits_of_num[0]) + int(digits_of_num[1])
    sum_of_second_half = int(digits_of_num[2]) + int(digits_of_num[3])
    if sum_of_first_half != sum_of_second_half:
        print("Эх, не повезло... Это НЕ счастливый билет!")
    else:
        print("Урааа! Счастливый Билет!")

# task 2
nNum = int(input("Enter a six-digit number: "))
if nNum < 100000 or nNum > 999999:
    print("Error: this num is not six-digit!")
else:
    str_nNum = str(nNum)
    first_half = str_nNum[0:3]
    rollSecond_half = first_half[::-1]
    if str_nNum[3:6] == rollSecond_half:
        print("Это чсило палиндром")
    else:
        print("Это число НЕ палиндром")

# task 3
R = 4
x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))
if x > 3 or x < -3 and y > 3 or y < -3:
    print("Эта точка НЕ лежит внутри круга")
else:
    print("Эта точка внутри круга")

