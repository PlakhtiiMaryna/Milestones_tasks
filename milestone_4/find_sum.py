def find_sum(target: int, li: list[int]) -> tuple[int, int]:
    result = []
    for i in range(len(li)):
        for j in range (i+1, len(li)):
            if li[i] + li[j] == target:
                result.append((i, j))
    return result



assert find_sum(9, [1, 2, 3, 4, 5, 7, 9, 8]) 
print(find_sum(9, [1, 2, 3, 4, 5, 7, 9, 8]))

print(f'Оскільки маємо вкладений цикл, то часова складність: O(n**2).\nПросторова складність O(N) — оскільки ми використовуємо не тільки змінні для ітерації та перевірки,\nа й створюємо додатковий список куди зберігаємо результати.')


def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
    result = {}
    for i, num in enumerate(li):
        calculate = target- num
        if calculate in result:
            print ((result[calculate], i))
        result[num] = i

find_sum_fast(15, [1, 2, 3, 4, 5, 7, 9, 8, 10,15,36])

print(f'Часова складність алгоритму O(N), оскільки ми проходимо в циклі по списку лише один раз.\nПросторова складність O(N), оскільки ми використовуємо додатково словник для збереження результатів ітерування,\nа це використання додаткової памєє''яті.')