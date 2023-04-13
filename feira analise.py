frutas = ['tomate','laranja', 'abacaxi','limao']
aumentou = 0
diminuiu = 0

def boaFeira():
    print('boa feira!')

print('Temos',frutas)
escolher_fruta = input('Escolha a fruta que deseja saber a inflacao \n')


if(escolher_fruta=='tomate'):
    preco_anterior = float(input('Digite o valor na semana passada \n'))
    preco_atual = float(input('Digite o valor atual \n'))
    if(preco_atual > preco_anterior):
        aumentou = preco_atual - preco_anterior
        print('O tomate aumentou R${:.2f}'.format(aumentou))
        boaFeira()
    elif(preco_atual < preco_anterior):
        diminuiu = preco_anterior - preco_atual
        print('O tomate diminuiu R${:.2f}'.format(diminuiu))
        boaFeira()
    else: 
        print('Não houve alteracao no tomate') 
        boaFeira() 

elif(escolher_fruta=='laranja'):
    preco_anterior = float(input('Digite o valor na semana passada \n'))
    preco_atual = float(input('Digite o valor atual \n'))
    if(preco_atual > preco_anterior):
        aumentou = preco_atual - preco_anterior
        print('A laranja aumentou R${:.2f}'.format(aumentou))
        boaFeira()
    elif(preco_atual < preco_anterior):
        diminuiu = preco_anterior - preco_atual
        print('A laranja diminuiu R${:.2f}'.format(diminuiu))
        boaFeira()
    else: 
        print('Não houve alteracao na laranja')
        boaFeira()  
     

elif(escolher_fruta=='abacaxi'):
    preco_anterior = float(input('Digite o valor na semana passada \n'))
    preco_atual = float(input('Digite o valor atual \n'))
    if(preco_atual > preco_anterior):
        aumentou = preco_atual - preco_anterior
        print('O abacaxi aumentou R${:.2f}'.format(aumentou))
        boaFeira()
    elif(preco_atual < preco_anterior):
        diminuiu = preco_anterior - preco_atual
        print('O abacaxi diminuiu R${:.2f}'.format(diminuiu))
        boaFeira()
    else:
        print('Não houve alteracao no abacaxi')  
        boaFeira()  

elif(escolher_fruta=='limao'):
    preco_anterior = float(input('Digite o valor na semana passada \n'))
    preco_atual = float(input('Digite o valor atual \n'))
    if(preco_atual > preco_anterior):
        aumentou = preco_atual - preco_anterior
        print('O limao aumentou R${:.2f}'.format(aumentou))
        boaFeira()
    elif(preco_atual < preco_anterior):
        diminuiu = preco_anterior - preco_atual
        print('O limao diminuiu R${:.2f}'.format(diminuiu))
        boaFeira()
    else: 
        print('Não houve alteracao no limao')  
        boaFeira()
else:
    print('Alimento nao disponivel na feira')






