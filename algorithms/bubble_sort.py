def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            draw_info.lst = lst
            yield True
            if ((lst[j] > lst[j+1] and ascending) or (lst[j] < lst[j+1] and not ascending)):

                lst[j], lst[j+1] = lst[j+1], lst[j]
