import pygame
import random

WIDTH = 1024
HEIGHT = 512
FPS = 30

# Задаем цвета
GRAY1= (192,192,192)
RED=(255,0,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


class Button:


    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("Black"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show1(self):
        screen.blit(button1.surface, (self.x, self.y))
    def show2(self):
        screen.blit(button2.surface, (self.x, self.y))
    def show3(self):
        screen.blit(button3.surface, (self.x, self.y))
    def show4(self):
        screen.blit(button4.surface, (self.x, self.y))
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
button1 = Button(
    "Инвентарь",
    (15, 255),
    font=30,
    bg="gray",
    feedback="You clicked me")
button2 = Button(
    "Характеристики",
    (155, 255),
    font=30,
    bg="gray",
    feedback="You clicked me")
button3 = Button(
    "Логи",
    (360, 255),
    font=30,
    bg="gray",
    feedback="You clicked me")
button4 = Button(
    "Опции",
    (430, 255),
    font=30,
    bg="gray",
    feedback="You clicked me")
# Цикл игры

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    button1.show1()
    button2.show2()
    button3.show3()
    button4.show4()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    pygame.draw.aaline(screen, RED, (250, 10), (250, 250))#Смотреть для моделек
    pygame.draw.aaline(screen, RED, (500, 10), (500, 250))
    pygame.draw.aaline(screen, RED, (750, 10), (750, 250))
    pygame.draw.aaline(screen, RED, (1000, 10), (1000, 250))
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 1004, 241), 2)
    pygame.draw.rect(screen, (0, 0, 0), (10, 260, 1004, 241), 2)
    pygame.display.flip()
    screen.fill(GRAY1)
pygame.quit()