n, m, q, cw, sw, hw, tw = map(int, input().split())

if n < 3 or m <= 0 or q <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
    print("Во введённых данных ошибка")
else:
    students = []
    totals = []
    error = False

    for _ in range(n):
        name = input()
        total = 0
        for j in range(m):
            a, b, c, d = map(int, input().split(","))
            total += a * cw + b * sw + c * hw + d * tw
        if total > q:
            error = True
        students.append((name, total))
        totals.append(total)

    if error:
        print("Во введённых данных ошибка")
    else:
        percents = [round((t / q) * 100) for t in totals]
        max_p = max(percents)
        min_p = min(percents)
        avg_p = round(sum(percents) / n)
        print(max_p, avg_p, min_p)

        students.sort(key=lambda x: x[1], reverse=True)

        for i in range(min(3, len(students))):
            name, total = students[i]
            print(f"{name} {round((total / q) * 100)}%")

        if avg_p <= 50:
            print("Курс усваивается плохо")
        else:
            print("Курс усваивается хорошо")
