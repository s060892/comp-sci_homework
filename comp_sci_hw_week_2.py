grades = [
    [85, 90, 58, 92],
    [92, 78, 95, 89],  
    [76, 64, 80, 87]
]

total = 0
min = grades[0][0]
max = grades[0][0]
for i in range(len(grades)):
    for j in range(len(grades[i])):
        total += grades[i][j]
        average = total / (len(grades) * len(grades[i]))
        if grades[i][j] < min:
            min = grades[i][j]
        if grades[i][j] > max:
            max = grades[i][j]

print("Total = ", total)
print("Average = ", average)
print("Range = ", max - min)
print("Min = ", min)
print("Max = ", max)
