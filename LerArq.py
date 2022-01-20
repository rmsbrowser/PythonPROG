ref_arquivo = open("apctest.log","r")
i=1
novalinha=""
for linha in ref_arquivo:
    if (len(linha)>2):
        novalinha=novalinha+linha.strip()+";"
    if (len(linha)==1):
        print(novalinha,i)
        novalinha=""    
    i=i+1
ref_arquivo.close()
