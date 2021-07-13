def conversor(tipo,valor):
    pesos = input("Por favor ingresa el valor de los pesos "+tipo)
    pesos = float(pesos)
    valor_dolar = valor
    dolares = pesos / valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print (valor, " pesos " ,tipo ," equivalen a" ,dolares, " dolares")


menu="""
Bienvenido 👀👀
1- COL PESOS
2- ARG PESOS
3- MEX PESOS

Elige opcion: """

opcion = int(input(menu))
if opcion==1:
    conversor("Pesos Colombianos ",3875)

elif opcion==2:
    conversor("Pesos Arg ",65)

elif opcion==3:
    conversor("Pesos Mex ",24)

else:    
    print (" Error de captura")

