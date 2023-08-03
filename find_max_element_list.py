def find_max_element(input_list):
    if not input_list:
        raise ValueError("Your List is Empty")

    #     Initializing first element as maximum element
    max_element = input_list[0]

    #
    for num in input_list:
        if num > max_element:
            max_element = num

    return max_element


def find_min_element(input_list):
    if not input_list:
        raise ValueError("Your List is Empty")
    #     Initializing first element as minimum element
    min_element = input_list[0]

    for num in input_list:
        if num < min_element:
            min_element = num
    return min_element


def find_sum_of_elements(input_list):
    if not input_list:
        raise ValueError("Your List is Empty")
    sum_of_elements = 0

    for num in input_list:
        sum_of_elements = sum_of_elements + num
    return sum_of_elements




def find_even_nums():

    even_nums = []
    for num in range(1, 1001):
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums
def find_odd_nums():

    odd_nums = []
    for num in range(1, 1001):
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums
def find_sorted_ascending(input_list):
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list

def find_sum_of_corresponding_elements(input_list, input_list3):
    # # List Should be same Length
    # result = []
    #
    # for i in range(len(input_list3)):
    #     if input_list[i] == len(input_list):
    #      result.append(input_list[i] + input_list3[i])
    # return result

    result = []
    max_length = max(len(input_list), len(input_list3))
    print(input_list)
    print(input_list3)
    for i in range(max_length):
        sum = 0
        if i < len(input_list):
            sum += input_list[i]
        if i < len(input_list3):
            sum += input_list3[i]
        print("SUM>>>",sum)
        result.append(sum)
    return result
def find_common_elements_in_both_list(input_list1, input_list2):
    # [(list1[0], list2[0]), (list1[1], list2[1])...] use zip
    result = []
    for i in range(len(input_list1)):
        for j in range(len(input_list2)):
            if input_list1[i] == input_list2[i] and input_list1[i] not in result:
                result.append(input_list1[i])
    return result
    # x = zip(input_list1, input_list2)
    # result = list(x)

    return result
def find_all_elements_both_list(input_list, input_list2):
    result = []
    # for num in range(len(my_list)):
    #     if input_list[num] not in result:
    #         result.append(input_list[num])
    # for num in range(len(my_list2)):
    #     if input_list2[num] not in result:
    #         result.append(input_list2[num])
    for element in input_list + input_list2:
        if element not in result:
            result.append(element)
    return result
def is_sorted_in_non_decresing_order(input_list):
    for num in range(0, len(input_list)-1):
        if input_list[num] > input_list[num+1]:
            return False
    return True


def find_num_of_occurance_of_element(input_list, element):
    counter = 0
    # dict = {ele1 : 1, ele2: 3, ... }
    # dict.get(element, 0)
    for num in range(len(input_list)):
        if input_list[num] == element:
            counter = counter + 1
    return counter
def find_frequeency_of_each_element(input_list):
    counter = 0
    dict = {}
    for i in range(len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i]  == input_list[j]:
                counter = counter + 1
                dict[input_list[i]] = counter
        counter = 0
    return dict
def find_list_without_duplicate(input_list):
    result = []
    for num in input_list:
        if num not in result:
            result.append(num)
    return result
def find_even_elements_from_list(input_list):
    result = []
    for num in range(len(input_list)):
        if input_list[num] % 2 == 0:
            result.append(input_list[num])
    return result
def print_list_in_reverse(input_list):
    reverse_list = []
    for num in range(len(input_list)-1, 0, -1):
        reverse_list.append(input_list[num])
    return reverse_list






if __name__ == '__main__':


    my_list = [12, 67, 87, 98, 2, 45]
print(my_list)
my_list2 = [34, 56, 34, 67, 45, 34, 45]
my_list4 = [10, 34, 56, 34, 67]
my_list3 = [25, 57, 31, 89, 43, 97, 76]



sum_of_corresponding_in_list = find_sum_of_corresponding_elements(my_list, my_list3)
print("Sum of corresponding elements in list",sum_of_corresponding_in_list)





common_in_both_list = find_common_elements_in_both_list(my_list, my_list2)
print("Common Elements In Both List", common_in_both_list)






all_elements_in_both_list = find_all_elements_both_list(my_list, my_list2)
print("All Elements In 2 Lists Withut Duplicates Are :", all_elements_in_both_list)

max_element = find_max_element(my_list)
print("Maximum Element in List is", max_element)
min_element = find_min_element(my_list)
print("Minimum Element in List is", min_element)
sum_of_elements = find_sum_of_elements(my_list)
print("Sum of Elements is ", sum_of_elements)

even_nums = find_even_nums()
print("Even Numbers In Range Of 1 to 1000", even_nums)
odd_nums = find_odd_nums()
print("Odd Numbers In Range Of 1 to 1000", odd_nums)








my_dict = find_frequeency_of_each_element(my_list2)
print("Frequency of each elements : ", my_dict)

num_of_occurence_element = find_num_of_occurance_of_element(my_list2, 34)
print("Number of occurence a given element : ", num_of_occurence_element )





list_without_duplicate = find_list_without_duplicate(my_list2)
print("List after removing duplicates :", list_without_duplicate)





even_elements = find_even_elements_from_list(my_list)
print("Even Elements From List", even_elements)




list_in_reverse = print_list_in_reverse(my_list2)
print(">>>>>>>>", list_in_reverse)
is_sorted = is_sorted_in_non_decresing_order(my_list)
print(is_sorted)

sorted_list_ascending = find_sorted_ascending(my_list)
print(sorted_list_ascending)






