def sumValues(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size - 1] + sumValues(lst, size - 1)

def countEvens(lst, size):
    if size == 0:
        return 0
    else:
        last_element_is_even = lst[size - 1] % 2 == 0
        rest_of_list_count = countEvens(lst, size - 1)
        return rest_of_list_count + (1 if last_element_is_even else 0)

if __name__ == "__main__":
    values = [8, 6, 7, 5, 3, 0, 9]
    sum_result = sumValues(values, len(values))
    print(f"The sum of values in the list is: {sum_result}")
    count_result = countEvens(values, len(values))
    print(f"The number of even values in the list is: {count_result}")
