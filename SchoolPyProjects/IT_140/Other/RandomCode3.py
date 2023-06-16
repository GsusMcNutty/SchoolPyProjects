def swap(v_list):
    list_len = len(v_list) - 1
    to_first = v_list[list_len]
    to_last = v_list[0]
    v_list[0] = to_first
    v_list[list_len] = to_last

    return v_list


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
