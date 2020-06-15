for flower in range(0, 1000):
    a = flower // 100
    b = flower // 10 % 10
    c = flower % 10
    if flower == a ** 3 + b ** 3 + c ** 3:
        print(flower)
