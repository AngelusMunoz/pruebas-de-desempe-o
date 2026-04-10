#Escalera Simulador

#Primero vamos a definir cuantas pisos hay en un edificio

pisos = 5   #Esto es para definir cuantos pisos hay en el edificio

#Ahora vamos a darle una bienvenida al usuario

print("Bienvenido a este simulador de 'Bajando las escaleras paso a paso y no caerme en el proceso' ¡Iniciemos!")
print("Estamos en un edificio de", pisos)

#Ahora vamos a hacer la accion de bajar paso a paso y no rodar hasta llegar al piso 1!

#Esto es para contar paso por paso
for piso in range(pisos,0,-1):
    #Este print solo es para saber en que piso estamos      
    print("Piso actual:", piso)
    
    #Aca le estamos pidiendo al usuario que interactue con nosotros para bajar
    input("Presione enter para bajar al siguiente piso")    
    piso = piso - 1

#Al llegar al piso 1, ya finalizamos en bajar las escaleras. Ahora vamos a darle una despedida al usuario
print("Alto ahi, amigo, ya estamos en el primer piso, ¡felicidades por bajar las escaleras paso a paso! ¡Que tengas un buen dia!")
