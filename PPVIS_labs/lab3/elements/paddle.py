import pygame 

class Paddle:
    
    def __init__(self, WIDTH, HEIGHT, paddle_w: int = 140, paddle_h: int = 16, paddle_speed: int = 5, paddle_xy = None) -> None:
        if paddle_xy:
            paddle_x = paddle_xy[0]
            paddle_y = HEIGHT - paddle_h - 10
        else:
            paddle_x = WIDTH // 2 - paddle_w // 2
            paddle_y = HEIGHT - paddle_h - 10
        self.paddle = pygame.Rect(
            paddle_x, 
            paddle_y,
            paddle_w, 
            paddle_h
        )
        self.w = paddle_w
        self.h = paddle_h
        self.speed = paddle_speed