# водятся названия городов в одну строку через пробел. 
# На основе этой строки необходимо создать список lst и добавить его в начало другого списка:
# cities = ["Москва", "Тверь", "Вологда"]
# Вывести результат на экран командой: print(*lst)


input_cities = input().split()
cities = ["Москва", "Тверь", "Вологда"]

print(*(input_cities + cities))