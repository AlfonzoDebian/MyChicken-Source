import pygame
import sys

pygame.init()

yVentana = 500
xVentana = 500

# Colores
rojo = (255, 0, 0)
amarillo = (255, 200, 0)
verde = (0, 250, 0)
azul = (0, 0, 255)
blanco = (255, 255, 255)

ventana = pygame.display.set_mode((yVentana, xVentana))
pygame.display.set_caption("Prototipo - Chicken")

# Pollo
polloSprite = pygame.image.load("img/pollo.png")
# Carro
CarroSprite = pygame.image.load("img/carro.png")

background = pygame.image.load("img/Baack.png")
font = pygame.font.Font("KiwiSoda.ttf", 40)

xPollo = 230
yPollo = 400
velocidadPollo = 10  

vidas = 3  

carros = [
    {"x": 200, "y": 250, "velocidad": 5, "colisionado": False},
    {"x": 200, "y": 330, "velocidad": 3, "colisionado": False},
    {"x": 100, "y": 190, "velocidad": 4, "colisionado": False},
    {"x": 50, "y": 110, "velocidad": 6, "colisionado": False},
]

Cerrar = True

while Cerrar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Cerrar = False

        #  pollo con teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and xPollo > 0:
                xPollo -= velocidadPollo
            if event.key == pygame.K_d and xPollo < yVentana - 50: 
                xPollo += velocidadPollo
            if event.key == pygame.K_w and yPollo > 0: 
                yPollo -= velocidadPollo
            if event.key == pygame.K_s and yPollo < xVentana - 50:
                yPollo += velocidadPollo

    ventana.fill((0, 0, 0))  
    ventana.blit(background, (0, 0))
    texto_vidas = font.render(f"Vidas: {vidas}", True, blanco)
    ventana.blit(texto_vidas, (10, 10))

   


    ventana.blit(polloSprite, (xPollo, yPollo))
   
    
    for carro in carros:
        carro["x"] += carro["velocidad"]
      
        if carro["x"] > yVentana:
            carro["x"] = -50  
            carro["colisionado"] = False  

      
        if (xPollo < carro["x"] + 50 and xPollo + 50 > carro["x"] and
            yPollo < carro["y"] + 50 and yPollo + 50 > carro["y"] and 
            not carro["colisionado"]):
            vidas -= 1
            carro["colisionado"] = True         
            if vidas <= 0:
                print("¡Game Over!")
                Cerrar = False

        ventana.blit(CarroSprite, (carro["x"], carro["y"]))

    pygame.display.update()
    pygame.time.delay(30)  

pygame.quit()
