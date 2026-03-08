def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
   
        for j in range(i,0,-1):
            draw_info.lst = lst
            yield True
            if ((ascending and lst[j]<lst[j-1]) or ((not ascending) and lst[j]>lst[j-1])):
                lst[j], lst[j-1] = lst[j-1], lst[j]
