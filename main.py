from classe import*
from views import*

def criar_cao():
    nome = input('Nome do cao: ')
    tamanho = input('Tamanho em CM: ')
    raca = input('Raca do cao: ')
    cao = Cachorro (nome,tamanho,raca)
    

def criar_humano():
    nome = input('Nome da pessoa: ')
    tamanho = input('Tamanho em CM: ')
    idade = input('Idade da pessoa: ')
    humano = Humano (nome,tamanho,idade)
    

while True: 
    menu_principal()
    op=int(input('Informe uma opcao: '))
    if 1 == op:
        criar_cao()

    if 2 == op:
        criar_humano()
    
        
        




