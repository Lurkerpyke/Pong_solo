import pygame, sys

#Configurações Iniciais
pygame.init()
clock = pygame.time.Clock()


#Configurações da tela principal
screen_width = 1080
screen_height = 2015
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')


#Retângulos do jogo
ball = pygame.Rect(screen_width/2 - 40, screen_height/2 - 40, 80, 80)
player = pygame.Rect(screen_width/2 - 125, screen_height - 20, 250, 50)
screen_rect = screen.get_rect()


#Velocidade da bola
ball_speed_x = 7
ball_speed_y = 7


#Cores
bg_color = pygame.Color('grey12')
lightgrey = (200, 200, 200)


#Funcões
def ball_animation():
    #Usando a variável global para modificar ela
    global ball_speed_x, ball_speed_y
    
    #Colisão da bola com a tela
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.bottom >= screen_height:
        pygame.quit()
        sys.exit()
    
    #Colisão da bola com os jogadores
    if ball.colliderect(player):
        if ball_speed_x < 30 and ball_speed_y < 30:
            ball_speed_x += 1
            ball_speed_y += 1
        ball_speed_y *= -1


#Observa se houve algum toque
tocou_player = False


#Loop principal
while True:
    # Respondendo os inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Trata o evento de toque do player
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player.collidepoint(event.pos):
                tocou_player = True
                # Ponto Inicial
                pygame.mouse.get_rel()
            elif event.type == pygame.MOUSEBUTTONUP:
                tocou_player = False

    #Movimentaçao do player e aumento de velocidade da bola
    if tocou_player:
        # Obtém o movimento do mouse apenas no eixo X
        rel_player_x, _ = pygame.mouse.get_rel()
        player.x += rel_player_x  # Move o jogador apenas na direção horizontal

        # Restringe o jogador aos limites da tela
        if player.left < 0:
            player.left = 0
        elif player.right > screen_width:
            player.right = screen_width
    
    
    #Configuração da bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    ball_animation()
    
    #Visual do jogo
    screen.fill(bg_color)
    pygame.draw.rect(screen, lightgrey, player)
    pygame.draw.ellipse(screen, lightgrey, ball)
    pygame.draw.aaline(screen, lightgrey, (0, screen_height/2), (screen_width, screen_height/2))
    

    #Atualizando a tela
    pygame.display.flip()
    clock.tick(60)

