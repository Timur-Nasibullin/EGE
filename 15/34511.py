# После сокращения выражения подставляем его в if
for a in range(26):
    f = True
    for x in range(26):
        # Обратное условие, чтобы найти, нарушается ли условие
        if not(x&25 == 0 or x&19 != 0 or x&a !=0):
            f = False
    if f:
        print(a)
        break