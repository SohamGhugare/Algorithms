data = [5, 7, 1, 9, 0, 3, 4, 2, 6, 8]

def selection_sort(data):
    for i in range(len(data)-1):
        min_val = i

        for j in range(i+1, len(data)):
            if data[j] < data[min_val]:
                min_val = j

        if min_val != i:
            data[min_val], data[i] = data[i], data[min_val]


selection_sort(data)
print(data)