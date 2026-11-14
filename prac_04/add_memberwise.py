# ATTEMPT 1
# def add_memberwise(first_list, second_list):
#     new_list = []
#     if len(first_list) >= len(second_list):
#         for index, value in enumerate(first_list):
#             if index < len(second_list):
#                 new_list.append(first_list[index] + second_list[index])
#             else:
#                 new_list.append(first_list[index])
#     else:
#         for index, value in enumerate(second_list):
#             if index < len(first_list):
#                 new_list.append(first_list[index] + second_list[index])
#             else:
#                 new_list.append(second_list[index])
#     return new_list

# ATTEMPT 2
def add_memberwise(first_list, second_list):
    new_list = []
    max_length = max(len(first_list), len(second_list))

    for i in range(max_length):
        value_1 = first_list[i] if i < len(first_list) else 0
        value_2 = second_list[i] if i < len(second_list) else 0
        new_list.append(value_1 + value_2)
    return new_list


print(add_memberwise([1, 2, 3], [2, 4, 6]))
print(add_memberwise([1, 2, 3, 4], [1, 2, 3]))
print(add_memberwise([1, 2], [1, 2, 3, 4, 5, 5]))
print(add_memberwise([], [1, 2, 3, 4]))
