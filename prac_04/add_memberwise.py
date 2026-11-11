def add_memberwise(first_list, second_list):
    new_list = []
    if len(first_list) >= len(second_list):
        for index, value in enumerate(first_list):
            if index < len(second_list):
                new_list.append(first_list[index] + second_list[index])
            else:
                new_list.append(first_list[index])
    else:
        for index, value in enumerate(second_list):
            if index < len(first_list):
                new_list.append(first_list[index] + second_list[index])
            else:
                new_list.append(second_list[index])
    return new_list


print(add_memberwise([1, 2, 3], [2, 4, 6]))
print(add_memberwise([1, 2, 3, 4], [1, 2, 3]))
print(add_memberwise([1, 2], [1, 2, 3, 4, 5, 5]))
print(add_memberwise([], [1, 2, 3, 4]))
