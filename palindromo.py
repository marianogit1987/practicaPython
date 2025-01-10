"""
Crear un Detector de palíndromos. Un palíndromo es una palabra o frase que se lee igual
 de derecho y del revés Ej anita lava la tina, neuquen, etc

"""

def polindomo(texto):
    #convierte a minuscula y verifica alfanumerico
    texto = "".join([caracter.lower() for caracter in frase if caracter.isalnum()])
    #compara texto con su reverso
    return texto == texto[::-1]

frase = input("Ingrese una frase: ")

if polindomo(frase):
    print(f"{frase} es un palindromo.")
else:
    print(f"{frase} no es un palindromo.")
     
#el siguiente codigo funciona con palabras unicas    
palabra = input("Ingrese una palabra: ")
if palabra == palabra[::-1]:
    print(f"{palabra} es un palindromo.")
else:
    print(f"{palabra} no es un palindromo.")
    