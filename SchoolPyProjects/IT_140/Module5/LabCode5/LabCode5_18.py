
def swap_values(val1, val2):
    return val2, val1


if __name__ == '__main__':
    user_val1 = input()
    user_val2 = input()
    user_val1, user_val2 = swap_values(user_val1, user_val2)
    print(user_val1, user_val2)
    ''' Type your code here. Your code must call the function. '''
