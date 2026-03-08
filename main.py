import pygame
from draw_info import DrawInformation
from drawing import draw
from utils import generate_starting_list
from algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort

pygame.init()


def main():
    run = True
    sorting = False
    ascending = True

    clock = pygame.time.Clock()

    n = 200
    min_val = 0
    max_val = 1000

    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(800,600,lst)

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
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
