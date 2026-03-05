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

    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 35)
    SIDE_PAD = 100
    TOP_PAD = 150

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

        self.block_width = round((self.width - self.SIDE_PAD)/len(lst))
        self.block_height = round((self.height-self.TOP_PAD)/(self.max_val-self.min_val))
        self.start_x = self.SIDE_PAD // 2


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

    timer_text = draw_info.LARGE_FONT.render(
        f"Time: {elapsed_time:.2f}s", 1, draw_info.BLACK)
    draw_info.window.blit(timer_text,
        (5, 30))

    controls = draw_info.FONT.render(
        "R - Reset | A - Ascending | D - Descending",
        1, draw_info.BLACK)
    draw_info.window.blit(controls,
        (draw_info.width/2 - controls.get_width()/2, 45))

    sorting_controls = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | M - Merge Sort",
        1, draw_info.BLACK)
    draw_info.window.blit(sorting_controls,
        (draw_info.width/2 - sorting_controls.get_width()/2, 75))

    space_color = draw_info.RED if sorting else draw_info.BLACK
    start_text = draw_info.FONT.render(
        "SPACE - Start Sorting", 1, space_color)
    draw_info.window.blit(start_text,
        (draw_info.width/2 - start_text.get_width()/2, 105))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i*draw_info.block_width
        y = draw_info.height - (val-draw_info.min_val)*draw_info.block_height

        color = draw_info.GRADIENTS[i%3]

        pygame.draw.rect(
            draw_info.window,
            color,
            (x,y,draw_info.block_width,draw_info.height)
        )


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):

            if ((lst[j] > lst[j+1] and ascending) or (lst[j] < lst[j+1] and not ascending)):

                lst[j], lst[j+1] = lst[j+1], lst[j]

                draw_info.lst = lst
                yield True

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
   
        for j in range(i,0,-1):
            if ((ascending and lst[j]<lst[j-1]) or ((not ascending) and lst[j]>lst[j-1])):
                lst[j], lst[j-1] = lst[j-1], lst[j]

                draw_info.lst = lst
                yield True
        
def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    yield from recursive_merge_sort(draw_info, 0, len(lst) - 1, ascending)

def recursive_merge_sort(draw_info, left, right, ascending):
    if left < right:
        mid = (left + right) // 2
        yield from recursive_merge_sort(draw_info, left, mid, ascending)
        yield from recursive_merge_sort(draw_info, mid + 1, right, ascending)
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
        if (ascending and leftList[i] <= rightList[j]) or (not ascending and leftList[i] >= rightList[j]):
            lst[k] = leftList[i]
            i += 1
        else:
            lst[k] = rightList[j]
            j += 1
        k += 1
        yield True

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

def main():
    run = True
    sorting = False
    ascending = True

    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 80

    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(800,600,lst)

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    start_time = 0
    elapsed_time = 0

    while run:
        clock.tick(60)

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

            elif event.key == pygame.K_SPACE and not sorting:
                if sorting_algorithm:
                    sorting = True
                    start_time = pygame.time.get_ticks()
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

    pygame.quit()


if __name__ == "__main__":
    main()