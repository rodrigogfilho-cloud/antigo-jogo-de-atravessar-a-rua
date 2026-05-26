import pygame

pygame.init()

cores = {
    "VERMELHO" : (255,0,0),
    "VERDE DE PASTO" : (70,255,70),
    "PRETO"  : (0,0,0)
}

clock = pygame.time.Clock()
#cria a janela do jogo
tela = pygame.display.set_mode((1700,900))
fundo = pygame.image.load("src/img/rua.png")
fundo = pygame.transform.scale(fundo,(1700,900))

#alterar o nome do jogo
pygame.display.set_caption("Joguinho do Mr. Godoy Master Aurudo 6️⃣7️⃣")

davi_x = 800
davi_y = 700
pos_x= -100
pos_x2 = 1800
pos_x3 = -250
#alterando a cor da tela (se torna inútil, pois coloquei depois)
#tela.fill(cores["VERMELHO"])


#carregando imagens 
davizinho = pygame.image.load("src/img/DAVI-BRITO.png")
davizinho = pygame.transform.scale_by (davizinho,0.5)
davizinhotwo = pygame.image.load("src/img/davi_lindo.png")
davizinhotwo = pygame.transform.scale_by(davizinhotwo,1)
carro = pygame.image.load("src/img/vilao.png") #Carrega uma imagem externa para dentro do jogo
carro = pygame.transform.scale_by (carro,1)
sacha = pygame.image.load("src/img/vilao2.png")
sacha = pygame.transform.scale_by(sacha,0.7)
bambam = pygame.image.load("src/img/vilao3.png")
bambam = pygame.transform.scale_by(bambam,0.7)

####################################################################
while True:
    #Pego todos os eventos que aconteceram na janela
    lista_de_eventos = pygame.event.get()
    #Percorro os eventos para encontrar aquele que eu quiser
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT: #Se um dos eventos for ter clicado no X eu encerro o programa
            pygame.quit()
            exit()

        
#PINTANDO A TELA NOVAMENTE
    
    tela.blit(fundo,(0,0))
    #INSERINDO O DAVI BRITO NA TELA
    tela.blit(davizinho,(davi_x,davi_y))
    tela.blit(carro,(pos_x,300))
    tela.blit(sacha,(pos_x2,420))
    tela.blit(bambam,(pos_x3,560))

    pos_x += 10
    if pos_x == 1800:
        pos_x = -60
    pos_x2 -= 10
    if pos_x2 == -120:
        pos_x2 = 1800
    pos_x3 += 10
    if pos_x3 == 1800:
        pos_x3= 200

    tecla_pressionada = pygame.key.get_pressed() # retorna a tecla que eu estou pressionando
    
        ###MOVIMENTAÇÃO DO DAVIZINHO CALABRESO###
    if tecla_pressionada [pygame.K_RIGHT] or tecla_pressionada [pygame.K_d]:
        if davi_x < 1700 - davizinho.get_width(): # arrumado*
            davi_x += 10
    if tecla_pressionada [ pygame.K_LEFT]or tecla_pressionada [pygame.K_a]:     
        if davi_x > 0:
            davi_x -= 10
    if tecla_pressionada [pygame.K_UP]or tecla_pressionada [pygame.K_w]:
        if davi_y > 0 :
            davi_y -= 10
    if tecla_pressionada [pygame.K_DOWN]or tecla_pressionada [pygame.K_s]:
        if davi_y < 900 - davizinho.get_height():
            davi_y += 10 # arrumado*

    #ATUALIZA A TELA
    pygame.display.update()

    clock.tick(60)
