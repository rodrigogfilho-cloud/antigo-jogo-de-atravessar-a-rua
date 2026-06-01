import pygame
from classe_viloes_hahaha import Viloes

class Jogador:
    def __init__ (self):
        self.davi_x = 800
        self.davi_y = 700
        #carregando imagens 
        self.davizinho = pygame.image.load("src/img/DAVI-BRITO.png")
        self.davizinho = pygame.transform.scale_by (self.davizinho,0.5)
    def andar_player(self,tela_do_game):
        
        tela_do_game.blit(self.davizinho,(davi_x,davi_y))
        tecla_pressionada = pygame.key.get_pressed() # retorna a tecla que eu estou pressionando
    
        if tecla_pressionada [pygame.K_RIGHT] or tecla_pressionada [pygame.K_d]:
            if davi_x < 1700 - self.davizinho.get_width(): # arrumado*
                davi_x += 10
        if tecla_pressionada [ pygame.K_LEFT]or tecla_pressionada [pygame.K_a]:     
            if davi_x > 0:
                davi_x -= 10
        if tecla_pressionada [pygame.K_UP]or tecla_pressionada [pygame.K_w]:
            if davi_y > 0 :
                davi_y -= 10
        if tecla_pressionada [pygame.K_DOWN]or tecla_pressionada [pygame.K_s]:
            if davi_y < 900 - self.davizinho.get_height():
                davi_y += 10 # arrumado*
    def exibir_player (self,tela_do_game):
        tela_do_game.blit(self.davizinho,(self.davi_x,self.davi_y))