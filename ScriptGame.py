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

ventana = pygame.display.set_mode((yVentana, xVentana))
pygame.display.set_caption("Prototipo - Chicken")

# Posición inicial y velocidad del pollo
xPollo = 230
yPollo = 400
velocidadPollo = 10  

# Número de vidas
vidas = 3  

# Posición y velocidad de los carros
carros = [
    {"x": 200, "y": 250, "velocidad": 5},
    {"x": 200, "y": 330, "velocidad": 3},
    {"x": 100, "y": 190, "velocidad": 4},
    {"x": 50, "y": 110, "velocidad": 6},
]

Cerrar = True

while Cerrar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Cerrar = False

        # Movimiento del pollo con teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and xPollo > 0:
                xPollo -= velocidadPollo
            if event.key == pygame.K_d and xPollo < yVentana - 50: 
                xPollo += velocidadPollo
            if event.key == pygame.K_w and yPollo > 0: 
                yPollo -= velocidadPollo
            if event.key == pygame.K_s and yPollo < xVentana - 50:
                yPollo += velocidadPollo

    # Movimiento de los carros
    for carro in carros:
        carro["x"] += carro["velocidad"]
        
        # Si el carro sale de la pantalla, reaparece al otro lado
        if carro["x"] > yVentana:
            carro["x"] = -50  

    # Detección de colisión
    for carro in carros:
        if (xPollo < carro["x"] + 50 and xPollo + 50 > carro["x"] and
            yPollo < carro["y"] + 50 and yPollo + 50 > carro["y"]):
            vidas -= 1
            print(f"¡Cuidado! Te quedan {vidas} vidas.")

            # Si el jugador pierde todas sus vidas, el juego termina
            if vidas <= 0:
                print("¡Game Over!")
                Cerrar = False

    ventana.fill((0, 0, 0))  
    pygame.draw.rect(ventana, rojo, (0, 50, 900, 50))
    pygame.draw.rect(ventana, rojo, (0, 400, 900, 50))
    pygame.draw.rect(ventana, amarillo, (0, 240, 900, 10))
    pygame.draw.rect(ventana, verde, (xPollo, yPollo, 50, 50))  

    # Dibujar los carros
    for carro in carros:
        pygame.draw.rect(ventana, azul, (carro["x"], carro["y"], 50, 50))

    pygame.display.update()
    pygame.time.delay(30)  

pygame.quit()
