import sys
import pygame
import random
import time

pygame.init()
pygame.font.init()

LARGEUR, HAUTEUR = 800, 800
taille_fenetre = (LARGEUR, HAUTEUR)

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
CELL_SIZE = 40

form = ["O", "I", "S", "Z", "L", "J", "T"]
direction = ["Down", "Right", "Up", "Left"]
pieces = []

fonts = pygame.font.Font(None, 25)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Tetris")
fenetre.fill(NOIR)

class Piece:
  def __init__(self):
    self.form = "J"#form[random.randint(0, len(form) - 1)]
    self.dataX = [0]
    self.dataY = [0]
    self.dataDirection = ["Down"]
    self.isBlock = False 

  def checkPiece(self):
      pass

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
        pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 2, CELL_SIZE * 2))
    elif self.form == "I":
        if self.dataDirection[0] == "Up" or self.dataDirection[0] == "Down":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 4))
        else:
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
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
        elif self.dataDirection[0] == "Right":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 3, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Down":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE * 2, CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Left":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE * 3, CELL_SIZE))
    elif self.form == "J":
        if self.dataDirection[0] == "Up":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Right":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE * 3, CELL_SIZE))
        elif self.dataDirection[0] == "Down":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE * 2, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
        elif self.dataDirection[0] == "Left":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 3, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE * 2, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
    elif self.form == "T":
        if self.dataDirection[0] == "Up":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE * 3, CELL_SIZE))
        elif self.dataDirection[0] == "Right":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Down":
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0], self.dataY[0], CELL_SIZE * 3, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif self.dataDirection[0] == "Left":
            pygame.draw.rect(fenetre, BLANC , pygame.Rect(self.dataX[0], self.dataY[0] + CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(fenetre, BLANC, pygame.Rect(self.dataX[0] + CELL_SIZE, self.dataY[0], CELL_SIZE, CELL_SIZE * 3))
    pygame.display.flip()

piece = Piece()
pieces.append(piece)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pieces[0].dataX.insert(0, pieces[0].dataX[0] - CELL_SIZE)
            elif event.key == pygame.K_UP:
                currentDirection = direction.index(pieces[0].dataDirection[0])
                if currentDirection == 3:
                    currentDirection = 0
                else :
                    currentDirection += 1
                pieces[0].dataDirection.insert(0, direction[currentDirection])
            elif event.key == pygame.K_RIGHT:
                pieces[0].dataX.insert(0, pieces[0].dataX[0] + CELL_SIZE)

    fenetre.fill(NOIR)
    for currentPiece in pieces:
        currentPiece.draw()
    if(piece.isBlock != True) :
        pieces[0].isBlocked()
        pieces[0].pieceMove()
        pieces[0].checkPiece()
    else :
        del piece
        piece = Piece()
        pieces.insert(0, piece)

    time.sleep(0.5)