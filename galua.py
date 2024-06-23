import itertools


def combinations(list_, ord):
    list_tmp = []
    for i in itertools.product(list_, repeat=ord):
        list_tmp.append(i)

    print("Все возможные комбинации коэффициентов для многочленов степени", ord)
    for t in list_tmp:
        if ord == 2:
            print(f"{t[0]}x + {t[1]}")
        elif ord == 3:
            print(f"{t[0]}x^2 + {t[1]}x + {t[2]}")
        elif ord == 4:
            print(f"{t[0]}x^3 + {t[1]}x^2 + {t[2]}x + {t[3]}")


def build_gf_2_2():
    # 1. Элементы простого конечного поля GF(2)
    gf_2_elements = [0, 1]
    print("\nЭлементы простого конечного поля GF(2):", gf_2_elements)

    # 2. Проверка неприводимости многочлена x^2 + x + 1
    print("\nПроверка неприводимости многочлена x^2 + x + 1.")
    print("Многочлен x^2 + x + 1 неприводим над GF(2), так как он не имеет корней в GF(2).")

    # 3. Элементы поля Галуа GF(2^2)
    gf_2_2_elements = ["0", "1", "α", "α + 1"]
    print("\nЭлементы поля Галуа GF(2^2):", gf_2_2_elements)

    # 4. Таблицы сложения и умножения в поле GF(2^2)
    addition_table = {
        '0': {'0': '0', '1': '1', 'α': 'α', 'α + 1': 'α + 1'},
        '1': {'0': '1', '1': '0', 'α': 'α + 1', 'α + 1': 'α'},
        'α': {'0': 'α', '1': 'α + 1', 'α': '0', 'α + 1': '1'},
        'α + 1': {'0': 'α + 1', '1': 'α', 'α': '1', 'α + 1': '0'}
    }

    multiplication_table = {
        '0': {'0': '0', '1': '0', 'α': '0', 'α + 1': '0'},
        '1': {'0': '0', '1': '1', 'α': 'α', 'α + 1': 'α + 1'},
        'α': {'0': '0', '1': 'α', 'α': 'α + 1', 'α + 1': '1'},
        'α + 1': {'0': '0', '1': 'α + 1', 'α': '1', 'α + 1': 'α'}
    }

    print("\nТаблица сложения:")
    for row in gf_2_2_elements:
        print(f"{row}: {addition_table[row]}")

    print("\nТаблица умножения:")
    for row in gf_2_2_elements:
        print(f"{row}: {multiplication_table[row]}")

    return gf_2_2_elements, addition_table, multiplication_table


def investigate_gf_2_2(elements, addition_table, multiplication_table):
    # 4. Мультипликативная группа
    multiplicative_group = elements[1:]
    print("\nМультипликативная группа:", multiplicative_group)

    # 5. Порядки всех элементов и образующие группы
    orders = {}
    generators = []

    for element in multiplicative_group:
        power = element
        order = 1
        while power != '1':
            order += 1
            power = multiplication_table[power][element]
        orders[element] = order
        if order == len(multiplicative_group):
            generators.append(element)

    print("\nПорядки элементов:")
    for element, order in orders.items():
        print(f"{element}: {order}")

    print("\nОбразующие группы:", generators)

    # 6. Все циклические подгруппы
    cyclic_subgroups = {}

    for element in generators:
        power = element
        cyclic_subgroup = [power]
        for _ in range(1, orders[element]):
            power = multiplication_table[power][element]
            cyclic_subgroup.append(power)
        cyclic_subgroups[element] = cyclic_subgroup

    print("\nЦиклические подгруппы:")
    for generator, subgroup in cyclic_subgroups.items():
        print(f"{generator}: {subgroup}")

    # 7. Диаграмма подгрупп
    print("\nДиаграмма подгрупп:")
    print("{1, α, α + 1}")
    print("  |")
    print("{1}")


def main():
    while True:
        try:
            field_order = int(input("Введите порядок конечного поля (например, 2 для GF(2^2)): "))
            if field_order != 2:
                print("На данный момент поддерживается только GF(2^2). Попробуйте снова.")
                continue

            combinations([0, 1], 2)

            gf_2_2_elements, addition_table, multiplication_table = build_gf_2_2()
            investigate_gf_2_2(gf_2_2_elements, addition_table, multiplication_table)
            break

        except ValueError:
            print("Введите корректное целое число. Попробуйте снова.")


if __name__ == "__main__":
    main()
