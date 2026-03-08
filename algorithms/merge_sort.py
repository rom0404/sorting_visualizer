def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    yield from merge_sort_helper(draw_info, 0, len(lst) - 1, ascending)


def merge_sort_helper(draw_info, left, right, ascending):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort_helper(draw_info, left, mid, ascending)
        yield from merge_sort_helper(draw_info, mid + 1, right, ascending)
        yield from merge_combine(draw_info, left, mid, right, ascending)


def merge_combine(draw_info, left, mid, right, ascending):
    lst = draw_info.lst
    num1 = mid - left + 1
    num2 = right - mid

    left_list = lst[left:mid + 1]
    right_list = lst[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < num1 and j < num2:
        yield True
        if (ascending and left_list[i] <= right_list[j]) or (not ascending and left_list[i] >= right_list[j]):
            lst[k] = left_list[i]
            i += 1
        else:
            lst[k] = right_list[j]
            j += 1
        k += 1

    while i < num1:
        lst[k] = left_list[i]
        i += 1
        k += 1
        yield True

    while j < num2:
        lst[k] = right_list[j]
        j += 1
        k += 1
        yield True
