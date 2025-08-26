"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
def verificar_palindromo(texto):
    # Remove espaços e pontuação, e converte para minúsculas
    texto = texto.replace(" ", "").lower()
    texto = ''.join(c for c in texto if c.isalnum())
    # Verifica se o texto é igual ao seu reverso
    """if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"
        """
    
    invertido = ''
    for letra in texto:
        invertido = letra + invertido

    if texto == invertido:
        return "Sim"
    else:
        return "Não"


texto = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(texto)
print(f"É um palíndromo? {resultado}")
