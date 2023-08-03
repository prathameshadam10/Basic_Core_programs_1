input_list = [7, 2, 90, 10, 75]

# output = [2, 1, 5, 3, 4]
my_list = input_list.copy()
# input_list.sort()


for i in range(0, len(input_list) - 1):
    for j in range(0, len(input_list) - i - 1):
        if input_list[j] > input_list[j + 1]:
            input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

print(my_list)
print(input_list)
result = []
for i in range(0, len(input_list)):
    for j in range(0, len(input_list)):
        if my_list[i] == input_list[j]:
            result.append(j + 1)

print(result)
