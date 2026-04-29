import pygame

pygame.mixer.init()


def load_music(file):
    pygame.mixer.music.load(file)


def play():
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def stop():
    pygame.mixer.music.stop()