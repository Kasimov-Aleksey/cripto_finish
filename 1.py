import math
from typing import List


def check_gcd(index: int) -> List[int]:
    # Все элементы кольца
    Z = [i for i in range(index)]

    # Наибольшие общие делители
    all_gcd = [1]

    for ni in Z[2:]:
        gcd = math.gcd(ni, index)
        if gcd == 1:
            all_gcd.append(ni)
            print(f"НОД({ni},{index}) = {gcd},следовательно {ni} ∈  ℤ*{index} ")
        else:
            print(f"НОД({ni},{index}) = {gcd},следовательно {ni} ∉  ℤ*{index} ")
    print()
    print(f"Группа обратимых элементов кольца классов вычетов по модулю {index} имеет следующий вид:")
    print(f"ℤ*{index} = {set(Z)}")
    return all_gcd


index = int(input("index = "))
all_gcd = check_gcd(index)

print(f"Данное кольцо классов вычетов состоит из {index} элементов")
print()
print(f"Образующие группу обратимых элементов Z*{index}")
print(f"Может быть записано следующим образом: ")
print(f"Z{index} = {set(all_gcd)}")
print(f"Размер группы обратимых элементов классов вычита : |Z*{index}| = {len(all_gcd)}")
print()

list_data_Hz = [] #создаем доп. список, где будем хранить все значения остатков H

for number, divider in enumerate(all_gcd):
    Hz = [1]
    degree = 1

    while True:
        H = (divider ** degree) % index
        degree += 1

        if H == 1:
            break
        Hz.append(H)
    print(f'O 〈 {divider} 〉 = {degree - 1}')
    print(f'H{number+1} = 〈 {divider} 〉 = \u007B {", ".join([str(i) for i in Hz])} \u007D')
    print()
    # print(f'O 〈 {divider} 〉 = {degree - 1}')


    list_data_Hz.append(set(Hz))


print('----------------------------------------------------------------')
print('FINAL')

# print(all_gcd)
# print(list_data_Hz)
# print()
check_similarity = []
for delite in list_data_Hz:
    # delite = list(delite) #нужно наладить  # налажено
    # print(delite)
    if not delite in check_similarity:
        check_similarity.append(delite)

# print(check_similarity)


upper = []
for index_check_similarity in range(len(check_similarity)):
    if check_similarity[index_check_similarity] == 1:
        continue
    for next_index_check_similarity in range(index_check_similarity+1,len(check_similarity)):
        result = all(elem in check_similarity[index_check_similarity] for elem in check_similarity[next_index_check_similarity])

        if result == True:
            upper.append(check_similarity[next_index_check_similarity])

#print(a)

# a = [[1, 4], [1, 4], [1, 4, 5]] проверка на одинаковые значения

new_upper = []
for u in upper:
    # u = list(u)
    if not u in new_upper:
        new_upper.append(u)

# print(new_upper)

print()
print()


num = 1

print(f"Z*{index} = { set(all_gcd) }")

for k in check_similarity:
    k = sorted(k)  # новая функция
    print(f"H({num})= \u007B {(', '.join([str(i) for i in k]))} \u007D")
    num += 1


print()

for k in check_similarity:
    num +=1

    for i in new_upper:

        if all(elem in k for elem in i) == True and i !=[1] and k !=[1] and i != k:


            print(f"H({check_similarity.index(i)+1}) = \u007B {(', '.join([str(k) for k in sorted(i)]))} \u007D  является подгруппой подгруппы H({check_similarity.index(k)+1}) = \u007B {(', '.join([str(i) for i in sorted(k)]))} \u007D")