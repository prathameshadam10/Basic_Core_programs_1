# Problem 4:
# Write a function that takes a list of integers and finds the length of the longest consecutive sequence of elements (ascending or descending).
#
# Example:
# ```python
# arr = [100, 4, 200, 1, 3, 2]
# print(longest_consecutive_sequence(arr))
# # Output: 4 (The longest consecutive sequence is [1, 2, 3, 4])
# ```
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(my_list[0:4:9])
# print(my_list[1:])
# print(my_list[3:])
# print(my_list[:6])
# print(my_list[::-1])
# print(my_list[-1:-3:-1])
my_dict = {"Name" : "Prathamesh", 1:[2, 4, 6, 8]}
print(my_dict["Name"])
print(my_dict.get(1))
my_s_dict = {x : x**3 for x in [1, 2, 3, 4, 5, 6]}
print(my_s_dict)
Tuple = ("jsxbui", "iienle")
print(Tuple)
Tuple = tuple(my_list)
print(Tuple[1])
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "Year" : 1964,

}
x = car.items()
print(x)
car.update({"Year": 2020})
print(car)
# for y in car:
#     print(y)
# for y in car:
#     print(car[y])
print(car.fromkeys())