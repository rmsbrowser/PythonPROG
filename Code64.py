
# uuencode e decode 64
# Ramsés Caldas

import base64
tocode=input("Entre com a String para Codificar...:")
tocode=tocode.encode() #Converte de String para Byte
encoded = base64.b64encode(tocode)
print("Valor codificado........:")
print(encoded)

todecode=input("Digite o Valor para Decodificar...:")
todecode=todecode.encode() # Converte de String para Byte
decoded= base64.b64decode(todecode)
print("Valor decodificado........:")
print(decoded)




