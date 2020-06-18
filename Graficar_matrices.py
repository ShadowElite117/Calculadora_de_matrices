from turtle import *
def dibujar_cuadricula():
    speed(0)
    color("cyan")
    for i in range(81):
        penup()
        goto(-40+i,-40)
        pendown()
        goto(-40+i,40)
        penup()
    for j in range(81):
        penup()
        goto(-40,-40+j)
        pendown()
        goto(40,-40+j)
        penup()

def graficar_matrices(n, matriz1, matriz2):
    color("black")
    speed(0)
    penup()
    goto(0,0)
    pendown()
    for i in range(n):
        for j in range(n):
            goto(matriz1[i][j], matriz2[i][j])
            
    exitonclick()

def main(n, matriz1, matriz2):
    speed(0)
    setworldcoordinates(-40,-40,40,40)
    setposition(0,0)
    clear()
    dibujar_cuadricula()
    setposition(0,0)
    setheading(0)
    pendown()
    color("black")
    for i in range(4):
        setposition(0,0)
        fd(100)
        right(90)
    penup()
    graficar_matrices(n, matriz1, matriz2)
    exitonclick()
    
    

