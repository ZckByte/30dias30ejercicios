# Crea un programa que implemente el Cifrado César, un método simple de cifrado por desplazamiento.  
# El programa debe:  
# - Pedir un mensaje y una clave de desplazamiento. ✅  
# - Cifrar el mensaje desplazando cada letra. ✅    
# - Poder descifrar el mensaje con la clave correcta. ✅  
# Extra: Permitir cifrar caracteres especiales y números sin alterarlos.

alfabeto = list("abcdefghijklmnopqrstuvwxyz")

mensaje = input("Ingrese el mensaje: ")
clave = int(input("Ingrese la clave de desplazamiento: "))

cifrado = ""

for i in range(len(mensaje)):
    if mensaje[i] in alfabeto:
        indice = alfabeto.index(mensaje[i])
        cifrado += alfabeto[indice + clave]

print(f"Palabra para cifra: {mensaje}\nClave de desplazamiento: {clave}\nPalabra Cifrada: {cifrado}")


        