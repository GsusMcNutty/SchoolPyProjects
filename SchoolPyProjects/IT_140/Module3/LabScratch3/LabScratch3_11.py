# Smallest number
number_list = [int(input('First Number?\n')), int(input('Second Number?\n')), int(input('Third Number?\n'))]


def sift(sift_list):
    index = int(sift_list[0])
    for i in sift_list:
        if i < index:
            index = i
    print(index)


sift(number_list)
