my_dict1 = {1: 23, 2: 34, 3: 15, 4: 63, 5: 52, 6: 100}

my_dict2 = {7: 37, 8: 82, 9: 27, 10: 99, 11: 51, 12: 42}

max_val = my_dict1.get(1)
print(max_val)
max_Val2 = list(my_dict2.values())[0]
print(max_Val2)


def find_merged_dict(input_dict1, input_dict2):
    result = {}
    for key, value in input_dict1.items():
        result[key] = value
    for key, value in input_dict2.items():
        result[key] = value
    return result


merged_dict = find_merged_dict(my_dict1, my_dict2)
print("Merged Dictionary :",merged_dict)

def find_max_value_in_dictionary(input_dict1):
     max_Values = list(input_dict1.values())[0]
     for value in input_dict1.values():
         if max_Values < value:
             max_Values = value
     return max_Values





max_Value = find_max_value_in_dictionary(my_dict1)
print("Maximum Element in Dict", max_Value)


def find_min_value_in_dictionary(input_dict1):
    min_Values = list(input_dict1.values())[0]
    for value in input_dict1.values():
        if min_Values > value:
            min_Values = value
    return min_Values
    pass


min_value = find_min_value_in_dictionary(my_dict1)
print("Minimum Element in Dict", min_value)
def find_sum_of_Values(input_dict1):
    total_sum = 0
    for value in input_dict1.values() :
        total_sum = total_sum + value
    return total_sum


sum_of_values = find_sum_of_Values(my_dict1)
print("Sum Of All Values in Dictionaries :", sum_of_values)