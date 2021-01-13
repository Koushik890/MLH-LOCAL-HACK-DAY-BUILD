lst_num = list()

nums = int(input("Enter the range of numbers: "))

for i in range(0, nums):
    num = int(input())
    lst_num.append(num)


def insertionsort(lst):
    for i in range(1, len(lst)):

        current_value = lst[i]
        current_position = i

        while current_position > 0 and current_value < lst[current_position-1]:
            lst[current_position] = lst[current_position -1]
            current_position -= 1
        
        lst[current_position] = current_value

    print(lst)

insertionsort(lst_num)
 



