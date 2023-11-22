intentos=3
contraseña=input("Contraseña: ")
intentos=intentos-1
while contraseña!="Eureka"and intentos>0:
    println("Contraseña incorrecta")
    contraseña=input("vuelve a introducir la contraseña ")
    intentos=intentos-1
if contraseña =="Eureka":
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

#Algoritmo Activitat2
#intentos <- 3
#Escribir 'Contraseña'
#Leer CONTRASENA
#intentos <- intentos -1
#Mientras Mayusculas(CONTRASENA)<>'EUREKA' Y intentos > 0 Hacer
#Escribir 'Contraseña incorrecta'
#Escribir 'Quedan ', intentos, ' intentos' 
#Escribir 'Vuelve a introducir la contraseña' 
#Leer CONTRASENA
#intentos<- intentos - 1
#FinMientras
#Si Mayusculas(CONTRASENA)='EUREKA' Entonces
#Escribir 'Contraseña correcta' 
#SiNo
#Escribir 'Contraseña incorrecta' 
#FinSi
#FinAlgoritmo