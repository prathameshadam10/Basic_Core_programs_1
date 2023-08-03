my_string = "hello world"


def find_count_of_char_in_string(input_string):
    my_dict = {}
    count_value = 0
    # "hello world"
    for i in range(len(input_string)):
        for j in range(len(input_string)):
            if input_string[i] == input_string[j]:
                count_value += 1
        my_dict[input_string[i]] = count_value
        count_value = 0
    return my_dict



count_of_char = find_count_of_char_in_string(my_string)
print("Count of char in String :", count_of_char)


def is_pallindrome_or_not(input_String):
    result_string = input_String[::-1]

    if input_String == result_string:
        print("Given String is Pallindrome")
    else:
        print("Given string is not Pallindrome")


_string = "hello world"
is_pallindrome_or_not(_string)



