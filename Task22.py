#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n – кол – во элементов первого  множества. m – кол – во элементов второго множества.
#Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение).


n = int(input("Введите число N элементов: "))
num_list_1 = []
for i in range(n):
    num = int(input("Введите num "))
    num_list_1.append(num)
print(num_list_1)

m = int(input("Введите число M элементов: "))
num_list_2 = []
for i in range(m):
    num = int(input("Введите num "))
    num_list_2.append(num)
print(num_list_2)

num_list3 = num_list_1 + num_list_2

print(num_list3)

num_count_dict = {}

for i in num_list3:
    if i in num_count_dict:
        num_count_dict[i] += 1
    else:
        num_count_dict[i] = 1

for num, count in num_count_dict.items():
    if count > 1:
        print(f"Число {num} встречается {count} раз(а)")
