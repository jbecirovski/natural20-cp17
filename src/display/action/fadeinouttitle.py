import functools

import pygame

from display import drawer
from display.action.client import POS_CHARACTER
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from util.geometry import Vector

IN_OUT_TIME_SECOND = 0.6

class FadeInOutTitleAction(IDomainAction):
    def __init__(self, in_fall):
        super().__init__()
        self.t = 0
        self.in_fall = in_fall

    def display(self, game_display, dt):
        sur = pygame.surface.Surface((800,600))
        self.t += dt/1000
        if self.in_fall:
            sur.set_alpha(255* self.t/IN_OUT_TIME_SECOND)
        else:
            sur.set_alpha(255* (1-self.t/IN_OUT_TIME_SECOND))
        if self.t > IN_OUT_TIME_SECOND:
            self.finished = True
        return functools.partial(game_display.blit, sur, (0,0))


#elapsed, start, end, total
def easing(t, b, c, d):
    t /= d
    return -c * t * (t - 2) + b;
