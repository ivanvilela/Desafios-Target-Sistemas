
#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json


with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)


if not dados:
    print("Não há dados disponíveis.")
    exit()


menor_faturamento = None
maior_faturamento = None
soma_faturamento = 0
contador_dias_com_faturamento = 0


for registro in dados:
    faturamento = registro['valor']  
    
    if faturamento > 0:
        
        if menor_faturamento is None or faturamento < menor_faturamento:
            menor_faturamento = faturamento
        if maior_faturamento is None or faturamento > maior_faturamento:
            maior_faturamento = faturamento
        
        
        soma_faturamento += faturamento
        contador_dias_com_faturamento += 1


if contador_dias_com_faturamento > 0:
    media_faturamento = soma_faturamento / contador_dias_com_faturamento
else:
    media_faturamento = 0


dias_acima_media = 0
for registro in dados:
    if registro['valor'] > media_faturamento:  
        dias_acima_media += 1


print("Menor faturamento:", menor_faturamento)
print("Maior faturamento:", maior_faturamento)
print("Número de dias acima da média:", dias_acima_media)
