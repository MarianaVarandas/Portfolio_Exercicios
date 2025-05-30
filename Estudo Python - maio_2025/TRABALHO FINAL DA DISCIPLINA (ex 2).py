#Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
#A Loja possui seguinte relação:

#Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
#Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
#Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;
#Elabore um programa em Python que: 
#Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 8];
#Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];
#Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
#Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
#Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
#Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
#Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
#Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
#Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
#Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
#Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
#Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  


print ("Seja muito bem-vinda, Mariana Varandas!\n")
print ("CONHEÇA O NOSSO CARDAPIO\n")
print ("CUPUAÇU (CP) - Tamanho P (P) - R$9,00")
print ("CUPUAÇU (CP) - Tamanho M (M) - R$14,00")
print ("CUPUAÇU (CP) - Tamanho G (G) - R$18,00\n")
print ("AÇAÍ (AC) - Tamanho P (P) - R$11,00")
print ("AÇAÍ (AC) - Tamanho M (M) - R$16,00")
print ("AÇAÍ (AC) - Tamanho G (G) - R$20,00\n")

soma = 0 #soma zero inserida antes da repetição para que não zere a cada novo pedido
while (True):
    sabor = input("Digite o sabor escolhido (CP/AC):")
    if (sabor != "AC" and sabor != "CP"):
        print ("Sabor inválido. Tente Novamente.\n")
        continue
    else:
        tam = input("Digite o tamanho escolhido (P/M/G):")
        if (tam != "P" and tam != "M" and tam != "G"):
            print ("Tamanho inválido. Tente Novamente.\n")
            continue
        else:
            if (sabor == "CP" and tam == "P"):
                print ("Você pediu um Cupuaçu tamanho P - R$9.00\n")
                v = 9
                soma = soma + v 
            elif (sabor == "CP" and tam == "M"):
                print ("Você pediu um Cupuaçu tamanho M - R$14.00\n")
                v = 14
                soma = soma + v
            elif (sabor == "CP" and tam == "G"):
                print ("Você pediu um Cupuaçu tamanho G - R$18.00\n")
                v = 18
                soma = soma + v  
            elif (sabor == "AC" and tam == "P"):
                print ("Você pediu um Açaí tamanho P - R$11.00\n")
                v = 11
                soma = soma + v
            elif (sabor == "AC" and tam == "M"):
                print ("Você pediu um Açaí tamanho M - R$16.00\n")
                v = 16
                soma = soma + v
            elif (sabor == "AC" and tam == "G"):
                print ("Você pediu um Açaí tamanho G - R$20.00\n")
                v = 20
                soma = soma + v
        ver = input("Deseja pedir mais alguma coisa? (S/N):")
        if (ver == "S"):
            continue #retorna a repetição desde while
        elif (ver == "N"):
            print (f"O valor total a ser pago é: RS{soma:.2f}")
            break #finalização da repetição

    

    
