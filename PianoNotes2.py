import pygame

pygame.mixer.init()

while True:
    note = pygame.mixer.Sound('notes/C4.wav')
    pygame.mixer.set_num_channels(13)
    note.set_volume(1)
    note.play()
    print(note)