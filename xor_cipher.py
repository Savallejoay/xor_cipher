import random

texto = "UIDE2026"
binario = ""

for letra in texto:
    binario += format(ord(letra), "08b")

llave = ""
for i in range(len(binario)):
    llave += str(random.randint(0,1))

cifrado = ""
for i in range(len(binario)):
    cifrado += str(int(binario[i]) ^ int(llave[i]))

descifrado = ""
for i in range(len(cifrado)):
    descifrado += str(int(cifrado[i]) ^ int(llave[i]))

resultado = ""
for i in range(0, len(descifrado), 8):
    resultado += chr(int(descifrado[i:i+8], 2))
    
print("texto:", texto)
print("Llave:", llave)
print("Cifrado:", cifrado)
print("Descifrado:", resultado)
