def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        best_idx = i
        for j in range(i + 1, len(lst)):
            if (ascending and lst[j] < lst[best_idx]) or (not ascending and lst[j] > lst[best_idx]):
                best_idx = j
            
            
            yield True

        if best_idx != i:
            lst[i], lst[best_idx] = lst[best_idx], lst[i]
            draw_info.lst = lst
            yield True
