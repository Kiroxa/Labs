from random import randrange as rnd
import pygame

class Ball:
    
    def __init__(self, WIDTH, HEIGHT, ball_radius: int = 9, ball_speed: int = 3, ball_xy = None) -> None:
        self.radius = ball_radius
        self.speed = ball_speed
        self.rect = int(ball_radius * 2 ** 0.5)
        if ball_xy:
            ball_x = ball_xy[0]
            ball_y = ball_xy[1]
        else:
            ball_x = rnd(self.rect, WIDTH - self.rect)
            ball_y = HEIGHT // 2
        self.ball = pygame.Rect(ball_x, ball_y, self.rect, self.rect)
        self.dx, self.dy = 1, -1