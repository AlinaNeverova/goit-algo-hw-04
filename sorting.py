import random
import timeit


# сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged


# сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


# Timsort
def timsort(arr):
    return sorted(arr)


# функція вимірювання часу виконання
def measure_sort_time(algorithm, data):
    data_copy = data.copy()
    start_time = timeit.default_timer()
    algorithm(data_copy)
    end_time = timeit.default_timer()
    return end_time - start_time


# набори даних для тестування
data_sizes = [1000, 5000, 10000, 20000, 40000]
results = {'Merge': [], 'Insertion': [], 'Timsort': []}
for size in data_sizes:
    random_data = [random.randint(0, 1000) for _ in range(size)]


# тестування
    results['Merge'].append(measure_sort_time(merge_sort, random_data))
    results['Insertion'].append(measure_sort_time(insertion_sort, random_data))
    results['Timsort'].append(measure_sort_time(timsort, random_data))


print(f"{'Size':<10}{'Merge':<15}{'Insertion':<15}{'Timsort':<15}")
for i, size in enumerate(data_sizes):
    print(f"{size:<10}{results['Merge'][i]:<15.5f}{results['Insertion'][i]:<15.5f}{results['Timsort'][i]:<15.5f}")


"""
Висновки:
1. Timsort (sorted) найшвидший на всіх обсягах даних.
2. Insertion Sort дуже повільний на великих масивах (O(n^2)), до 44 сек на 40k.
3. Merge Sort швидший за вставки, але стабільно повільніший за Timsort.
4. Timsort поєднує Merge і Insertion, тому вбудований sort() це найефективніший вибір у Python.
"""
