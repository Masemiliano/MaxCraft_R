bilden, x, y, namn = input("Bild: "), int(input("X: ")), int(input("Y: ")), input("Namn: ")

import pygame

pygame.init()

bild = pygame.image.load(bilden)

bild = pygame.transform.scale(bild, (int(x), int(y)))

pygame.image.save(bild, namn)
