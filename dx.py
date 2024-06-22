def evklid():
    data = [215, 1282]
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
    r = [y2,data[1]]
    return r
r = evklid()