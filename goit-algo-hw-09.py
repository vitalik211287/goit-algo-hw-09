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


