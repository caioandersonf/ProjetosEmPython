idade = int(input("Qual sua idade ?\n"))
nome = input("Qual seu nome ?\n")

nomes = nome.isalpha()

while(nomes != True):
    
    nome = input("Qual seu nome ?\n")

    nomes = nome.isalpha()

if(idade>=18):
    
    print("{} já pode tirar a carteira.\n".format(nome))

else:
    print("{} ainda não pode tirar a carteira.\n".format(nome))
    
    