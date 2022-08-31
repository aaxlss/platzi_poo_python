from distutils.archive_util import make_archive
from operator import le
import random

def merge_sort(list):
    print(f'original list: {list}')
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        print(f'left: {left}', '*' * 5, f'right: {right}');

        #recursive call
        print(f'sorting left side of the sublist')
        merge_sort(left)
        print(f'sorting right side of the sublist')
        merge_sort(right)

        #iterate to check both lists
        i = 0
        j = 0

        main_iterator = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                print(f'list position in main itereator: {list[main_iterator]}')
                print(f'index in left sublist: {left[i]}')
                list[main_iterator] = left[i]
                i += 1
            else:
                list[main_iterator] = right[j]
                j += 1

            main_iterator += 1

        while i < len(left):
            list[main_iterator] = left[i]
            i += 1
            main_iterator += 1

        while j < len(right):
            list[main_iterator] = right[j]
            j += 1
            main_iterator += 1

        print(f'left: {left}, right: {right}')
        print(list)
        print('-'* 50)

    return list



if __name__ == '__main__':
    list_length = int(input('Lenght list: '))

    list = [random.randint(0, 100) for i in range(list_length)]
    print (list)
    print('-' * 2)

    sorted_list = merge_sort(list)
    print(sorted_list)
