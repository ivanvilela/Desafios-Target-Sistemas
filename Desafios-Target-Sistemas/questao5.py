

#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

texto_entrada = input("Digite uma string para inverter: ")

def inverter(s):
    texto_invertido = ""

    for i in range(len(s) - 1, -1, -1):
        
         texto_invertido += s[i]
    
    return texto_invertido



texto_resultado = inverter(texto_entrada)
print("String invertida:", texto_resultado)