
#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

num = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))

def pertence_fibonacci(num, a=0, b=1):
    
    if num == a or num == b:
        return True
    
    if b > num:
        return False
   
    return pertence_fibonacci(num, b, a + b)

def verifica_fibonacci(num):
    if num < 0:
        return "O número não pode ser negativo."
    
    if pertence_fibonacci(num):
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


resultado = verifica_fibonacci(num)
print(resultado)

