def get_triangle(rows: int) -> list[list[int]]:
    triangle = []
    for i in range(rows):
        new_row = []  # Створюємо новий рядок
        for j in range(i + 1):
            if j == 0 or j == i:  # Перший і останній елементи рядка завжди 1
                new_row.append(1)
            else:
                value = triangle[i-1][j-1] + triangle[i-1][j]  # Інші елементи - сума двох чисел з попереднього рядка
                new_row.append(value)
        triangle.append(new_row)
    return triangle



# Отримання трикутника Паскаля та його друк
triangle = get_triangle(9)
max_width = len(' '.join(map(str, triangle[-1])))  # Ширина останнього рядка
for row in triangle:
    row_str = ' '.join(map(str, row))
    print(row_str.center(max_width))


