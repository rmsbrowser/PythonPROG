# Conversor de Arquivo by Ramses Augusto de Lima Caldas 
# Abril de 2020
import os

#Exemplo de arquivo : U:/TODELETE/syncterm.lst
nome_do_arquivo = input("Nome do Arquivo......................:")
imprime_sumario = input("Imprime Sumario S-Sim N-Nao..........:")
tipo_de_saida =   input("Tipo de Saida D-Decimal H-Hexadecimal:")
resultado =       input("Resultado  A-Arquivo T-tela..........:")

arq_saida = nome_do_arquivo+".out"
if resultado == "A" :
    arquivo_de_saida=open(arq_saida,"w")

tamanho_arquivo = os.path.getsize(nome_do_arquivo)

ref_arquivo = open(nome_do_arquivo,"rb")
i=1
x=range(tamanho_arquivo)
novalinha=""
digito_para_escrever=""
tabulacao = "\t"

for i in x:
    byte=ref_arquivo.read(1)
    num=int((ord(byte)))
    
    #print(byte)
    if resultado == "T" and tipo_de_saida == "H" :
        digito_para_escrever = hex(num)+" "
        novalinha=novalinha+digito_para_escrever+tabulacao
        #print(digito_para_escrever)
        #print(hex(num),"",end="")
                
    if resultado == "T" and tipo_de_saida == "D" :
        digito_para_escrever = str(num)+" "
        novalinha=novalinha+digito_para_escrever+tabulacao
        #print(digito_para_escrever)
        #print(num,"",end="")
          
    if resultado == "A" and tipo_de_saida == "H" :
        digito_para_escrever = hex(num)+" "
        arquivo_de_saida.write(digito_para_escrever)

    if resultado == "A" and tipo_de_saida == "D" :
        digito_para_escrever = str(num)+" "
        arquivo_de_saida.write(digito_para_escrever)

    i=i+1
    if i/10 == int(i/10) : 
       if resultado == "T" :
           print(novalinha)
       novalinha=""
       #print("") 
    #print(novalinha)

ref_arquivo.close()

if imprime_sumario == "S" :
    print("")
    print("Fim do Arquivo.")
    print("Tamanho do Arquivo...:",tamanho_arquivo)
    print("Bytes Lidos..........:",i)
    if resultado == "A" :
        print("Resultado em arquivo.:",arq_saida)
        arquivo_de_saida.close()

