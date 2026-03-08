def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    yield from quick_sort_helper(lst, 0, len(lst) - 1, ascending)


def quick_sort_helper(lst, start, end, ascending):
    if start < end:
        pivot_value = lst[start]
        left_mark = start + 1
        right_mark = end
        done = False

        while not done:
            if ascending:
                while left_mark <= right_mark and lst[left_mark] <= pivot_value:
                    left_mark += 1
                    yield True
                while right_mark >= left_mark and lst[right_mark] >= pivot_value:
                    right_mark -= 1
                    yield True
            else:
                while left_mark <= right_mark and lst[left_mark] >= pivot_value:
                    left_mark += 1
                    yield True
                while right_mark >= left_mark and lst[right_mark] <= pivot_value:
                    right_mark -= 1
                    yield True

            if right_mark < left_mark:
                done = True
            else:
                lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]
                yield True

        lst[start], lst[right_mark] = lst[right_mark], lst[start]
        yield True

        split_point = right_mark
        yield from quick_sort_helper(lst, start, split_point - 1, ascending)
        yield from quick_sort_helper(lst, split_point + 1, end, ascending)
