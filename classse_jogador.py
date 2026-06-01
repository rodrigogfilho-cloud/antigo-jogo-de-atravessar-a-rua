import pygame

class Jogador:
    def __init__ (self):
        self.davi_x = 800
        self.davi_y = 700
        #carregando imagens 
        self.imagem = pygame.image.load("src/img/DAVI-BRITO.png")
        self.imagem = pygame.transform.scale_by (self.imagem,0.5)

        self.tecla_pressionada = pygame.key.get_pressed()

    def andar_player(self,tela_do_game):
        tela_do_game.blit(self.imagem,(self.davi_x,self.davi_y))
        
    
        if self.tecla_pressionada [pygame.K_RIGHT] or self.tecla_pressionada [pygame.K_d]:
            if self.davi_x < 1700 - self.imagem.get_width(): # arrumado*
                self.davi_x += 10
        if self.tecla_pressionada [ pygame.K_LEFT]or self.tecla_pressionada [pygame.K_a]:     
            if self.davi_x > 0:
                self.davi_x -= 10
        if self.tecla_pressionada [pygame.K_UP]or self.tecla_pressionada [pygame.K_w]:
            if self.davi_y > 0 :
                self.davi_y -= 10
        if self.tecla_pressionada [pygame.K_DOWN]or self.tecla_pressionada [pygame.K_s]:
            if self.davi_y < 900 - self.imagem.get_height():
                self.davi_y += 10 # arrumado*

    def exibir_player (self,tela_do_game):
        tela_do_game.blit(self.imagem,(self.davi_x,self.davi_y))