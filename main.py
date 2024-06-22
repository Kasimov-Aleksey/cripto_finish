import math
import sys
from random import randrange

#шаг 1
def hash_bi(p,a,b,P,q, M): #q = O(P)

    print(f"Вход: M = {M}, p = {p}, a = {a}, b = {b}, P = {P}, 0(P) = {q}")
    n = int(math.log(q,2))
    print(f"n = log2 (q) = log2 ({q}) = {n}")
    data_ack_letter = []
    print("Перевод из символов в аски , а после в бинарь")
    for i in range(len(M)):
        letter = ord(M[i])
        print(f"        {M[i]} = {letter} = {bin(letter)[2:]}")
        data_ack_letter.append(bin(letter)[2:])
    bi_data = "".join(data_ack_letter)
    bi_data = "110110001100010111000010" # потом дропнуть
    bi_data = "0" * (n-len(bi_data)%n)+bi_data if not isinstance(bi_data, int) else bi_data
    list_bi_data = [bi_data[i:i+n] for i in range(0, len(bi_data), n)]
    print(bi_data)
    list_10_data = [int(bi_data[i:i + n],2) for i in range(0, len(bi_data), n)]
    h_m = bin(sum(list_10_data)%(2**n))[2:]
    print(f"{' + '.join(list_bi_data)} = {bin(sum(list_10_data))[2:]} mod 2^{5}= {h_m} ")
    return h_m

 
print()
# шаг 2
def point(h_m, q):
    a = h_m
    print(f"h(M) = a = в двоичной системе: {a} = в десятеричной системе: {int(a,2)}")
    e = int(int(a,2))%q
    print(f"{a} mod {q} = {e}")
    if e == 0:
        print(f"Приравниваем e к 1 (е = 1)")
        e = 1
    return e

# шаг 3
def point3(k, q):
    print(f"k = {k},   0 < k < {q}")

#шаг 4
def point4(k, q, P, a, b, p):
    print(f"C = k*P = {k}P ,   r = xc mod {q}")
    print(f"Нужно посчитать: 2P = P + P, 4P = 2P + 2P")
    x1, y1 = P[0], P[1]
    print(f"a = {a}, b = {b}, P = {P} --> x1 = {P[0]}, y1 = {P[1]} ")
    z = a
    for index in range(1,3):
        print(f"{2*index}P = {index}P + {index}P")
        while True:
            x3 = int(((3*x1**2+a)/(2*y1))**2-2*x1)%p
            if ((3*x1**2+a)/(2*y1)).is_integer():
                break
            a += p # менять для уменьшения расчета
        a = z
        print(f"((3*x1^2+(a))/(2*y1)^2 - 2x1 = (3*{x1}**2+({a}))/(2*{y1}))**2 - 2*{x1} = {x3}")
        while True:
            y3 = int(((3*x1**2+a)/(2*y1))*(x1-x3)-y1)%p
            if ((3*x1**2+a)/(2*y1)).is_integer():
                break
            a += p # менять для уменьшения расчета
        a = z
        print(f"((3*x1^2+(a))/(2*y1) * (x1-x3) - y1 = (3*{x1}**2+({a}))/(2*{y1}))**2 - 2*{x1} = {y3}")
        print(f"Проверка: y^2 = x^3 + {a}*x + {b}")
        print(f"(y^2) mod{p} = ({y3}^2)%p =  {(y3**2)%p}")
        print(f"(x^3 + {a}*x + {b}) mod {p} = ({x3}^3 + {a}*{x3} + {b}) mod{p} = ({x3**3} + {a*x3} + {b}) mod {p} = {(x3**3 + a*x3 + b)%p}")
        print()
        print(f"C = {k}P = ({x1}, {y1}) + ({x1}, {y1}) = ({x3}, {y3})")

        x1, y1 = x3, y3
        # x3,y3 = 48, 59 # удалить
    r = x3%q
    print()


    print(f"r = xc mod {q} = {r} ")
    if r == 0:
        print("Вернись на шаг 3 и выбери другую k")
        print("Вернись на шаг 3 и выбери другую k")
        print("Вернись на шаг 3 и выбери другую k")
        print("Вернись на шаг 3 и выбери другую k")
        print("Вернись на шаг 3 и выбери другую k")
        print("Вернись на шаг 3 и выбери другую k")
        sys.exit()


    return r
def point5(r, d, k,e, q):
    print(f"d - ключ подписи ( 0 < d < {q} ) ")
    print(f"d = {d}")
    s = (r*d + k*e)%q
    print(f"s = (r*d + ke) mod (q) = {r}*{d} + {k}*{e} mod {q} = {s}")
    return s

def point6(r,s,q):
    n = int(math.log(q, 2))
    r_bin = bin(r)[2:].zfill(n)
    s_bin = bin(s)[2:].zfill(n)
    print(f"r =  в десятичном системе счисления  {r} = в двоичном виде {r_bin}")
    print(f"s =  в десятичном системе счисления  {s} = в двоичном виде {s_bin}")
    print(f"Электронная подпись (ЭП) = r || s  = {r_bin} || {s_bin} = {r_bin+s_bin}")

def main():
    p = 97#103
    a = 9 #6
    b = 3#4
    P = (0,10) #(3, 7)
    q = 47 #59
    M = "ШЭВ"#"eoo"
    print(f"ШАГ-1")
    h_m = hash_bi(p, a, b, P, q, M)
    print()
    print(f"ШАГ-2")
    e = point(h_m, q)
    print()
    print(f"ШАГ-3")
    k = 4
    point3(k, q)
    print()
    print(f"ШАГ-4")
    r = point4(k, q, P, a, b, p)
    print()
    print(f"ШАГ-5")
    d = randrange(q-14, q+1)
    d = 37#32 # удалить
    k = 4#7 # удалить
    s = point5(r, d, k,e, q)
    print()
    print(f"ШАГ-6")
    point6(r, s, q)

main()