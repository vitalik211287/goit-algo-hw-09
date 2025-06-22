import heapq

def heap_sort(arr, descending=False):
    heap = []
    for el in arr:
        heapq.heappush(heap, el)  # просочування вгору — як у конспекті
    sorted_list = [heapq.heappop(heap) for _ in range(len(heap))]  # просочування вниз
    return sorted_list[::-1] if descending else sorted_list

# Тестування
arr = [12, 11, 13, 5, 6, 7]
print("Пірамідальне сортування за зростанням:", heap_sort(arr))
print("Пірамідальне сортування за спаданням:", heap_sort(arr, descending=True))


# ✅ Обов'язкове завдання: мінімальні витрати на з'єднання кабелів
# Алгоритм базується на черзі з пріоритетом з heapq (як у конспекті з прикладом про планування)

def min_total_cost(cables):
    heapq.heapify(cables)
    total = 0
    while len(cables) > 1:
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        merged = a + b
        total += merged
        heapq.heappush(cables, merged)
    return total

# Тестування
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_total_cost(cables))


# ✅ Додаткове завдання: злиття k відсортованих списків
# Використовується мінімальна купа, як рекомендовано в конспекті

def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (значення, індекс списку, позиція в списку)

    result = []
    while heap:
        val, list_idx, pos = heapq.heappop(heap)
        result.append(val)
        if pos + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][pos + 1]
            heapq.heappush(heap, (next_val, list_idx, pos + 1))

    return result

# Тестування
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("Результат злиття списків:", merge_k_lists(lists))