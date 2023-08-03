# Create a function that takes a string and returns a new string with its first and last characters swapped, except under two conditions:If the length of the string is less than two, return "Incompatible.".
# If the first and last characters are the same, return"Two's a pair.".
# ExamplesflipEndChars("Cat, dog, and mouse.") ➞ ".at, dog, and mouseC"
#
# flipEndChars("ada") ➞ "Two's a pair."
#
# flipEndChars("Ada") ➞ "adA"
#
# flipEndChars("z") ➞ "Incompatible."
_string = "Cat, dog, and mouse."
print(len(_string))
name = "Prathamesh adam"
print(len(name))


def flip_end_chars(my_string):
    if len(my_string) < 2:
        return "Incompatible"
    elif my_string[0] == my_string[-1]:
        return "Two's a pair."
    else:

        str2 = my_string[-1] + my_string[1:-2] + my_string[0]
        return str2


if __name__ == '__main__':

    stri = flip_end_chars(_string)
    print(stri)
