import pygame

from display import drawer
from display.action.interface import IDomainAction
from display.button import ButtonBuilder
from display.cache import ImagesCache
from display.spritesheet import SpriteSheet


class ButtonPushedAction(IDomainAction):

    def __init__(self, floor):
        self.floor = floor
        self.button = ButtonBuilder().get_button_for_floor(floor)
        self.persistent_name = 'button-{}'.format(self.floor)
        self.sound: pygame.mixer.SoundType = None

    def display(self, game_display, dt):
        self.sprite_sheet: SpriteSheet = ImagesCache().sprites_sheets[self.button.idx]
        self.image = self.sprite_sheet.get_element(0, 0)
        if self.sound is None:
            self.sound = pygame.mixer.Sound('resource/sounds/Button-push-1s.wav')
            self.sound.play()
        return drawer.add_image(game_display, self.image, self.button.coordinates, self.button.size)


class ButtonReleasedAction(IDomainAction):

    def __init__(self, floor):
        self.floor = floor
        self.button = ButtonBuilder().get_button_for_floor(floor)
        self.persistent_name = 'button-{}'.format(self.floor)

    def display(self, game_display, dt):
        self.sprite_sheet: SpriteSheet = ImagesCache().sprites_sheets[self.button.idx]
        self.image = self.sprite_sheet.get_element(0, 0)
        return drawer.add_image(game_display, self.image, self.button.coordinates, self.button.size)
