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
