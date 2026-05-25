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
#alterar o nome do jogo
pygame.display.set_caption("Joguinho do Mr. Godoy 6️⃣7️⃣")

davi_x = 0
davi_y = 0 


#alterando a cor da tela
tela.fill(cores["VERDE DE PASTO"])


#carregando imagens 
davizinho = pygame.image.load("src/img/DAVI-BRITO.png")
davizinho = pygame.transform.scale_by (davizinho,2)
davizinhotwo = pygame.image.load("src/img/davi_lindo.png")
davizinhotwo = pygame.transform.scale_by(davizinhotwo,2)
while True:
    #Pego todos os eventos que aconteceram na janela
    lista_de_eventos = pygame.event.get()
    #Percorro os eventos para encontrar aquele que eu quiser
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT: #Se um dos eventos for ter clicado no X eu encerro o programa
            pygame.quit()

        
#PINTANDO A TELA NOVAMENTE
    tela.fill(cores["VERDE DE PASTO"])

    #INSERINDO O DAVI BRITO NA TELA
    tela.blit(davizinho,(davi_x,davi_y))

    tecla_pressionada = pygame.key.get_pressed() # retorna a tecla que eu estou pressionando

    if tecla_pressionada [pygame.K_RIGHT] or tecla_pressionada [pygame.K_d]:
        if davi_x < 1700: # arrumar
            davi_x += 10

    if tecla_pressionada [ pygame.K_LEFT]or tecla_pressionada [pygame.K_a]:     
        if davi_x > 0:
            davi_x -= 10
    if tecla_pressionada [pygame.K_UP]or tecla_pressionada [pygame.K_w]:
        if davi_y > 0 :
            davi_y -= 10
    if tecla_pressionada [pygame.K_DOWN]or tecla_pressionada [pygame.K_s]:
        if davi_y < 900:
            davi_y += 10 # arrumar

    

    #ATUALIZA A TELA
    pygame.display.update()

    clock.tick(60)
    