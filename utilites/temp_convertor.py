t = int(input("Введите исходную температуру: "))
source = input("Исходный формат температуры(Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Reaumur, Romer): ")
target = input("Формат температуры на выходе(Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Reaumur, Romer): ")

def convert_to_cels(a, b):
    if a == "Kelvin":
        return b - 273.15
    elif a == "Fahrenheit":
        return (b - 32) * (5 / 9)
    elif a == "Rankine":
        return (b - 491.67) * (5 / 9)
    elif a == "Delisle":
        return 100 - (b * 2 / 3)
    elif a == "Newton":
        return b * (100 / 33)
    elif a == "Reaumur":
        return b * (5 / 4)
    elif a == "Romer":
        return (b - 7.5) * (40 / 21)
    elif a == "Celsius":
        return b

result_to_cels = convert_to_cels(source, t)

def convert_from_cels(a, b):
    if a == "Kelvin":
        return b + 273.15
    elif a == "Fahrenheit":
        return b * (9 / 5) + 32
    elif a == "Rankine":
        return (b + 273.15) * (9 / 5)
    elif a == "Delisle":
        return (100 - b) * (3/2)
    elif a == "Newton":
        return b * (33 / 100)
    elif a == "Reaumur":
        return b * (4 / 5)
    elif a == "Romer":
        return b * (21 / 40) + 7.5
    elif a == "Celsius":
        return b

end_result =  convert_from_cels(target, result_to_cels)

print(end_result)



    