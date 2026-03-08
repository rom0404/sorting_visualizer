import random
import pygame
pygame.init()


class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    BLUE = 0,0,255
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    FONT = pygame.font.SysFont('comicsans', 15)
    LARGE_FONT = pygame.font.SysFont('comicsans', 25)
    SIDE_PAD = 20
    TOP_PAD = 150
    BOTTOM_PAD = 10
    MIN_BAR_HEIGHT = 0

    def __init__(self,width,height,lst):
        self.width=width
        self.height=height

        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("sorting visualization")
        self.set_list(lst)
    
    def set_list(self,lst):
        self.lst=lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = (self.width - self.SIDE_PAD) / len(lst)
        
        range_val = self.max_val - self.min_val
        if range_val == 0:
            self.block_height = self.height - self.TOP_PAD - self.BOTTOM_PAD
        else:
            self.block_height = (self.height - self.TOP_PAD - self.BOTTOM_PAD) / range_val
            
        self.start_x = (self.width - (len(lst) * self.block_width)) / 2


def generate_starting_list(n,min_val,max_val):
    lst = []
    for _ in range (n):
        val = random.randint(min_val,max_val)
        lst.append(val)
    return lst


def draw(draw_info, algo_name, ascending, sorting, elapsed_time=0):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1, draw_info.BLUE)
    draw_info.window.blit(title,
        (draw_info.width/2 - title.get_width()/2, 5))

    timer_text = draw_info.FONT.render(
        f"Time: {elapsed_time:.2f}s", 1, draw_info.BLACK)
    draw_info.window.blit(timer_text,
        (5, 30))

    controls = draw_info.FONT.render(
        "R - Reset | A - Ascending | D - Descending",
        1, draw_info.BLACK)
    draw_info.window.blit(controls,
        (draw_info.width/2 - controls.get_width()/2, 35))

    sorting_controls1 = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | S - Selection Sort",
        1, draw_info.BLACK)
    draw_info.window.blit(sorting_controls1,
        (draw_info.width/2 - sorting_controls1.get_width()/2, 55))

    sorting_controls2 = draw_info.FONT.render(
        "M - Merge Sort | Q - Quick Sort",
        1, draw_info.BLACK)
    draw_info.window.blit(sorting_controls2,
        (draw_info.width/2 - sorting_controls2.get_width()/2, 75))

    space_color = draw_info.RED if sorting else draw_info.BLACK
    start_text = draw_info.FONT.render(
        "SPACE - Start Sorting", 1, space_color)
    draw_info.window.blit(start_text,
        (draw_info.width/2 - start_text.get_width()/2, 95))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        next_x = draw_info.start_x + (i + 1) * draw_info.block_width
        current_block_width = max(1, next_x - x) # Ensure at least 1px width
        
        # Calculate height from bottom, ensuring at least MIN_BAR_HEIGHT
        bar_height = (val - draw_info.min_val) * draw_info.block_height + draw_info.MIN_BAR_HEIGHT
        y = draw_info.height - bar_height - draw_info.BOTTOM_PAD

        color = draw_info.GRADIENTS[i%3]

        pygame.draw.rect(
            draw_info.window,
            color,
            (x, y, current_block_width, bar_height)
        )

    # Draw a baseline to verify the bottom boundary
    pygame.draw.line(draw_info.window, draw_info.BLACK, 
                     (draw_info.start_x, draw_info.height - draw_info.BOTTOM_PAD),
                     (draw_info.start_x + len(lst) * draw_info.block_width, draw_info.height - draw_info.BOTTOM_PAD), 2)


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            draw_info.lst = lst
            yield True
            if ((lst[j] > lst[j+1] and ascending) or (lst[j] < lst[j+1] and not ascending)):

                lst[j], lst[j+1] = lst[j+1], lst[j]

                

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
   
        for j in range(i,0,-1):
            draw_info.lst = lst
            yield True
            if ((ascending and lst[j]<lst[j-1]) or ((not ascending) and lst[j]>lst[j-1])):
                lst[j], lst[j-1] = lst[j-1], lst[j]

                


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
        
def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    yield from merge_sort_helper(draw_info, 0, len(lst) - 1, ascending)

def merge_sort_helper(draw_info, left, right, ascending):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort_helper(draw_info, left, mid, ascending)
        yield from merge_sort_helper(draw_info, mid + 1, right, ascending)
        yield from mergeCombine(draw_info, left, mid, right, ascending)

def mergeCombine(draw_info, left, mid, right, ascending):
    lst = draw_info.lst
    num1 = mid - left + 1
    num2 = right - mid

    leftList = lst[left:mid + 1]
    rightList = lst[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < num1 and j < num2:
        yield True
        if (ascending and leftList[i] <= rightList[j]) or (not ascending and leftList[i] >= rightList[j]):
            lst[k] = leftList[i]
            i += 1
        else:
            lst[k] = rightList[j]
            j += 1
        k += 1

    while i < num1:
        lst[k] = leftList[i]
        i += 1
        k += 1
        yield True

    while j < num2:
        lst[k] = rightList[j]
        j += 1
        k += 1
        yield True
    


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

def main():
    run = True
    sorting = False
    ascending = True

    clock = pygame.time.Clock()

    n = 300
    min_val = 0
    max_val = 1000

    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(800,600,lst)

    sorting_algorithm = merge_sort
    sorting_algo_name = "Merge Sort"
    sorting_algorithm_generator = None

    start_time = 0
    elapsed_time = 0

    while run:
        clock.tick(1440)

        if sorting:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False

        draw(draw_info, sorting_algo_name, ascending, sorting, elapsed_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            elif event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
                elapsed_time = 0
                start_time = 0

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_b and not sorting:
                sorting_algo_name = "Bubble Sort"
                sorting_algorithm = bubble_sort

            elif event.key == pygame.K_i and not sorting:
                sorting_algo_name = "Insertion Sort"
                sorting_algorithm = insertion_sort

            elif event.key == pygame.K_m and not sorting:
                sorting_algo_name = "Merge Sort"
                sorting_algorithm = merge_sort
            elif event.key == pygame.K_s and not sorting:
                sorting_algo_name = "Selection Sort"
                sorting_algorithm = selection_sort
            elif event.key == pygame.K_q and not sorting:
                sorting_algo_name = "Quick Sort"
                sorting_algorithm = quick_sort

            elif event.key == pygame.K_SPACE and not sorting:
                if sorting_algorithm:
                    sorting = True
                    start_time = pygame.time.get_ticks()
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

    pygame.quit()


if __name__ == "__main__":
    main()