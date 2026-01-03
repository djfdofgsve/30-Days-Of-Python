#Day 2: 30 Days of python programming
first_name = "Grigoriy"
last_name = "Pilipenko"
full_name = "Grigoriy Pilipenko"
country = "Russia"
city = "Moscow"
age = 18
year = 2026
is_married = False
is_light_on = True
personal_inf = {
    'first_name' : 'Grigoriy',
    'last_name' : 'Pilipenko',
    'age' : '18',
    'is_married' : 'no'
}

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(personal_inf))

print('First name length:', len(first_name))
print('lenth of last name:', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

r = float(input())
import math
area_of_circle = math.pi * r ** 2
print(area_of_circle)
import math
circum_of_circle = math.pi * 2 * r
print(circum_of_circle)

a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = input("В какой вы сейчас стране? ")
d = int(input("Введите сколько вам лет? "))
print("имя: " , a)
print("фамилия: " , b)
print("страна: " , c)
print("возраст: " , d)
