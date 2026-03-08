import pygame
from draw_info import DrawInformation


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
        "B - Bubble Sort | I - Insertion Sort | S - Selection Sort",
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
