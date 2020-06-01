# BUBBLE SORTING --- 
# Runs through each value in the list
# If one value is greater than its next value, it swaps its place
# Loops through the list several times

data = [5, 7, 1, 9, 0, 3, 4, 2, 6, 8]

def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

bubble_sort(data)
print(data)