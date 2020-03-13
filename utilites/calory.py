weigth = int(input("укажите свои параметры\n вес: "))
height = int(input("рост: "))
age = int(input("возраст: "))
gender = input("ваш пол м/ж: ")

def male_clc(w, h, a):
    return (88.362 + (13.397 * w) + (4.799 * h) - (5.677 * a)) * 1.375
clc_male = male_clc(weigth, height, age)

def fml_clc(w,h,a):
    return (447.593 + (9.247 * w) + (3.098 * h) - (4.330 * a)) * 1.375
clc_fml = fml_clc(weigth, height, age)

if gender == "м":
    print("Рекомендуемое количество калорий в день:", round(clc_male))

elif gender == "ж":
    print("Рекомендуемое количество калорий в день:", round(fml_clc))