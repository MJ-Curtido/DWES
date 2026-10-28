from estatistic_ex3 import average, limits

list_data = [1, 356, 74, 35, 67, 4, 6, 7, 87545, 5, 4434, 567, 435, 3245, 0, -4, 3, -2]

minimum, maximum = limits(list_data)
range_result = maximum - minimum

print(f'Average: {average(list_data)}')
print(f'Minimum: {minimum} - Maximum: {maximum}')
print(f'Range: {range_result}')
