import sys
import pygame
import random

pygame.init()
pygame.font.init()

LARGEUR, HAUTEUR = 800, 800
taille_fenetre = (LARGEUR, HAUTEUR)

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
CELL_SIZE = 40

form = ["O", "I", "S", "Z", "L", "J", "T"]
direction = ["Down", "Right", "Up", "Left"]

fonts = pygame.font.Font(None, 25)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Tetris")
fenetre.fill(NOIR)

class Piece:
  def __init__(self):
    self.form = form[random.randint(0, len(form) - 1)]
    self.dataX = [1]
    self.dataY = [1]
    self.dataDirection = [random.randint(0, len(direction) - 1)]
    self.isBlock = False

  def isBlocked(self):
    if self.form == "O":
        if self.dataY[0] >= LARGEUR - CELL_SIZE * 3:
            self.dataY.insert(0, self.dataY[0] - 1)
            self.isBlock = True
    elif self.form == "I":
        if self.dataDirection[0] == "Up" or self.dataDirection[0] == "Down":
            if self.dataY[0] >= LARGEUR - CELL_SIZE * 5:
                self.dataY.insert(0, self.dataY[0] - 1)
                self.isBlock = True
        else:
            if self.dataY[0] >= LARGEUR - CELL_SIZE * 2:
                self.dataY.insert(0, self.dataY[0] - 1)
                self.isBlock = True
    elif self.form == "S" or self.form == "Z" or self.form == "T" :
        if self.dataDirection[0] == "Up" or self.dataDirection[0] == "Down":
            if self.dataY[0] >= LARGEUR - CELL_SIZE * 3:
                self.dataY.insert(0, self.dataY[0] - 1)
                self.isBlock = True
        else:
            if self.dataY[0] >= LARGEUR - CELL_SIZE * 4:
                self.dataY.insert(0, self.dataY[0] - 1)
                self.isBlock = True
    else:
        if self.dataDirection[0] == "Up" or self.dataDirection[0] == "Down":
            if self.dataY[0] >= LARGEUR - CELL_SIZE * 4:
                self.dataY.insert(0, self.dataY[0] - 1)
                self.isBlock = True
        else:
            if self.dataY[0] >= LARGEUR - CELL_SIZE * 3:
                self.dataY.insert(0, self.dataY[0] - 1)
                self.isBlock = True

  def pieceMove(self):
    self.dataY.insert(0, self.dataY[0] + CELL_SIZE)

  def draw(self):
    if self.form == "O":
        pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE + CELL_SIZE, CELL_SIZE + CELL_SIZE))
    elif self.form == "I":
        if self.dataDirection[0] == "Up" or self.dataDirection[0] == "Down":
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 4))
        else:
            if self.dataX[0] + CELL_SIZE * 4 > 801:
                pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 4, CELL_SIZE))
    elif self.form == "S":
        if self.dataDirection[0] == "Up" or self.dataDirection[0] == "Down":
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE + CELL_SIZE, CELL_SIZE))
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE + CELL_SIZE, CELL_SIZE))
        else:
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 2))
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE + CELL_SIZE))
    elif self.form == "Z":
        if self.dataDirection[0] == "Down" or self.dataDirection[0] == "Up":
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE + CELL_SIZE, CELL_SIZE))
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE + CELL_SIZE, CELL_SIZE))
        else:
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE + CELL_SIZE))
          pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE + CELL_SIZE))
    elif self.form == "L":
        if self.dataDirection[0] == "Up":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE * 2, CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Right":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE * 3, CELL_SIZE))
        elif self.dataDirection[0] == "Down":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
        elif self.dataDirection[0] == "Left":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 3, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
    elif self.form == "J":
        if self.dataDirection[0] == "Up":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE * 2, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
        elif self.dataDirection[0] == "Right":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE * 3))
        elif self.dataDirection[0] == "Down":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Left":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 3, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
    elif self.form == "T":
        if self.dataDirection[0] == "Up":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataX[0], CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataX[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Right":
            pygame.draw.rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE * 3)
        elif self.dataDirection[0] == "Down":
            pygame.draw.rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3)
        elif self.dataDirection[0] == "Left":
            pygame.draw.rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3)
            pygame.draw.rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE)

def userInput():
    pass
    # User input

def move():
  piece.draw()
  if(piece.isBlock != True) :
    piece.isBlocked()
    piece.pieceMove()

move()

piece = Piece()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()