# def evklid():
#     data = [17, 8200]
#     a, b = max(data), min(data)
#     q, r, x, y = "-", "-", "-", "-"
#     x2, x1, y2, y1 = 1, 0, 0, 1
#     print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
#     while b != 0:
#         q, r = (a // b), (a % b)
#         x = (x2 - q * x1)
#         y = (y2 - q * y1)
#         a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
#         print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
#     r = [y2,data[1]]
#     return r
# r = evklid()
# #
# print(pow(149,-1,82620))
# print(r[0]%r[1])


#
# def char_to_binary(char):
#     binary_repr = bin(ord(char))[2:].zfill(8)
#     return binary_repr
#
# # Пример использования:
# char = 'e'
# binary = char_to_binary(char)
# print(f"Двоичное представление символа '{char}': {binary}")

# import math
# print(math.floor(math.log(83197, 2)))
# print(math.log(70181, 2))
# print(int("0101100010111", 2))
# print(bin(2839)[2:].zfill(13))
# print()
#
# print(pow( 7420 ,6753,8383))
# print(bin(3429)[2:].zfill(13))

# print(ord("e"))
# print(chr(101))
# print(bin(101)[2:].zfill(8))
# print(len("0000000000000"))


# print(bin(2839)[2:].zfill(13))



# def char_to_binary(char):
#     binary_repr = bin(ord(char))[2:].zfill(8)
#     return binary_repr
#
# # Пример использования:
# char = 'd'
# binary = char_to_binary(char)
# print(f"Двоичное представление символа '{char}': {binary}")
# print(int("0000000011010", 2))
# print(pow(613, 17, 8383))
# print(bin(0)[2:].zfill(13))
# print(len("00001010111000"))
# print(int("01001010000011", 2))
# print(pow(4739, 6753, 8383))
# print(bin(613)[2:].zfill(13)
# print(len("01110100"))
# print(int("01110100", 2))
# print(chr(101))







# def evklid():
#     data = [149, 82620]
#     a, b = max(data), min(data)
#     q, r, x, y = "-", "-", "-", "-"
#     x2, x1, y2, y1 = 1, 0, 0, 1
#     print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
#     while b != 0:
#         q, r = (a // b), (a % b)
#         x = (x2 - q * x1)
#         y = (y2 - q * y1)
#         a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
#         print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
#     r = [y2,data[1]]
#     return r
# r = evklid()
# #
# print(pow(149,-1,82620))
# print(r[0]%r[1])


# print(len("10000010110011011"))
# print(int("10011110010111100", 2))
# print(pow(16484, 149, 83197))
# print(bin(81084)[2:].zfill(16))
# print(int("66971", 2))

# print(pow(81084, 1109, 83197))
# print(bin(26725)[2:].zfill(16))

def evklid(e, φ):
    data = [e, φ]
    a, b = max(data), min(data)
    q, r, x, y = "-", "-", "-", "-"
    x2, x1, y2, y1 = 1, 0, 0, 1
    print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
    while b != 0:
        q, r = (a // b), (a % b)
        x = (x2 - q * x1)
        y = (y2 - q * y1)
        a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
        print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
    d = y2
    return d

print(f"Гененеция ключей ")
def gen_key():
    p, q = 271, 307 # меняем по таблице простых чисел
    print(f"    1) Выбор простых чисел: p = {p}, q = {q} ")
    n = p * q
    print(f"    2) Вычисление n путем произведения p на q:")
    print(f"𝑛 = 𝑝•𝑞 = {p} * {q} = {n}")
    φ = (p-1)*(q-1)
    print(f"    3) Вычисления функции Эйлера от n:")
    print(f"φ(𝑛) = (𝑝 − 1)•(𝑞 − 1) = {p-1}•{q-1} = {φ} ")
    print(f"    4)Выбор целого простого числа числа e, которое взаимно простое φ(n):")
    e = 149 # меняем по таблице простых чисел
    print(f"e = {e}" )
    print(f"    5)Найти экспоненту расшифрования d, удовлетворяющею условию e•d≡ 1(mod φ(n) )")
    print(      f"          Расширенный алгоритм Евклида")
    d = evklid(e, φ)
    print()
    print(f"d = e^(-1) mod (𝑛) = {e}^(-1) mod {φ} = {d}")
    print("###")
    print(f"Переписывать не надо. print(pow({e}, -1, {φ})) = {pow(e, -1, φ)}")
    print("###")
    print()
    data_key = {"open_key": (e, n), "close_key": (d, n)}
    print(f"    6)Генерация ключей")
    print(f"Публичный ключ  = (e,n) = ({e}, {n})")
    print(f"Частный ключ = (d,n) = ({d}, {n})")
    return data_key
data_key = gen_key()

