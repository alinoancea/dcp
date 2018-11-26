#!/usr/bin/env python3

def create_list_with_division(l):
    if len(l) == 1:
        return [0]

    product = 1

    for e in l:
        product *= e

    return [product // e for e in l]

def create_list_without_division(l):
    if len(l) == 1:
        return [0]

    result = [1 for _ in range(len(l))]

    first_product = 1
    last_product = 1
    for i in range(len(l)):
        result[i] *= first_product
        if not i:
            result[len(l) - 1] *= last_product

            last_product *= l[len(l) - 1]
        else:
            result[len(l) - i - 1] *= last_product

            last_product *= l[len(l) - i - 1]
        first_product *= l[i]
    return result


print(create_list_with_division([1, 2, 3, 4, 5]))
print(create_list_with_division([3, 2, 1]))

print(create_list_without_division([1, 2, 3, 4, 5]))
print(create_list_without_division([3, 2, 1]))
