import time

def voltar(delay):

        print("\Voltando...\n")
        time.sleep(delay)
        return

def lerOpcao(minimo, maximo, menu):
    while True:
        print(menu)
        try:
            opcao = int(input("\n| "))
            if opcao >= minimo and opcao <= maximo:
                return opcao
            else:
                print("\nOpção inválida! Selecione uma opção existente:\n")
                time.sleep(1)

        except:
            print("\nValor inválido!\n")
            time.sleep(1)

def lerInt(texto):
    while True:
        try:
            print(f"\n{texto}\n")
            opcao = int(input("| "))
            return opcao
        except:
            print("\nDigite um valor válido\n")
            time.sleep(1)

    
    


#----------------------------------LANCHONETE----------------------------------------------
def lanchonete():
    valorPedido = 0

    print("\nSeja bem vindo(a) a nossa lanchonete!\n")
    
    while True:
        menu = """Escolha seu pedido:

1 - Hamburguer | R$20,00
2 - Refrigerante | R$7,00
3 - Batata Frita | R$12,00
---------------------------
4 - Finalizar e pagar
0 - Cancelar e sair"""
        
        opcao = lerOpcao(0, 4, menu)
        

            
        if opcao == 0:
            voltar(2)

        elif opcao == 1:              
            print("\nHamburguer adicionado\n")
            valorPedido += 20
            print(f"Valor: R${valorPedido:.2f}\n".replace(".", ","))

        elif opcao == 2:                    
            print("\nRefrigerante adicionado\n")
            valorPedido += 7   
            print(f"Valor: R${valorPedido:.2f}\n".replace(".", ","))
                
        elif opcao == 3:
            print("\nBatata Frita adicionada\n")
            valorPedido += 12
            print(f"Valor: R${valorPedido:.2f}\n".replace(".", ","))

        elif opcao == 4:
            if valorPedido != 0:
                print(f"\nO seu pedido ficou no valor de R${valorPedido:.2f}\n\nAgradecemos pela preferência :)\n".replace(".", ","))
                break
            else:
                print("\nNão há nada para pagar, selecione um item ou cancele o pedido\n")
                time.sleep(2)
                

#----------------------------------CALCULADORA----------------------------------------------

def calculadora():
    
    print("\nBem vindo(a) à calculadora!\n")
    menu = """Selecione uma opção:

1 - Iniciar programa
2 - Sair"""

    
    opcao = lerOpcao(1, 2, menu)

    if opcao == 1:
        print("\nDigite seu primeiro número\n")
        nmr1 = int(input("| "))
        print("\nDigite seu segundo número\n")
        nmr2 = int(input("| "))
        
        menu = f"""
Escolha a operação que será realizada entre os números {nmr1} e {nmr2}
                
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Duvisão
--------------------------
0 - Voltar"""

        opcaoOperacao = lerOpcao(0, 4, menu)

        if opcaoOperacao == 0: 
            voltar(2)                                       
    
        elif opcaoOperacao == 1:
            print(f"\n{nmr1} + {nmr2} = {nmr1+nmr2}\n")
            time.sleep(2)

        elif opcaoOperacao == 2:
            print(f"\n{nmr1} - {nmr2} = {nmr1-nmr2}\n")
            time.sleep(2)
                
        elif opcaoOperacao == 3:
            print(f"\n{nmr1} * {nmr2} = {nmr1*nmr2}\n")
            time.sleep(2)

        elif opcaoOperacao == 4:
            print(f"\n{nmr1} / {nmr2} = {nmr1/nmr2:.2f}\n")
            time.sleep(2)

            
#----------------------------------CALCULADORA-IDADE----------------------------------------

def calculadoraIdade():
    
    print("\nBem vindo(a) à calculadora de idade!\n")
    while True:
        menu = """Selecione uma opção:

1 - Iniciar
2 - Sair"""
        opcao = lerOpcao(1, 2, menu)

        if opcao == 2:
            voltar(2)

        elif opcao == 1:
            
                anoNascimento = lerInt("Digite o ano de seu nascimento:")

                anoAtual = lerInt("Digite o ano atual:")
            

        menu = """
        Fez aniversário esse ano?

1 - Sim
2 - Não"""
            
        fezAniversario = lerOpcao(1, 2, menu)

        

        if fezAniversario == 1:
            print(f"\nVocê tem {anoAtual-anoNascimento} anos.")
            time.sleep(2)
            break
            
        elif fezAniversario == 2:
            print(f"\nVocê tem {(anoAtual-anoNascimento)-1} anos.")
            time.sleep(2)
            break

#----------------------------------CONVERSOR-TEMPERATURA----------------------------------------

def conversorTemperatura():
    print("\nBem vindo(a) ao conversor de temperatura\n")
    while True:
        menu = """Selecione uma opção:

1 - Iniciar
2 - Sair"""
        opcao = lerOpcao(1, 2, menu)

        if opcao == 2:
            voltar(2)

        elif opcao == 1:

            menu = """
            Selecione a unidade que deseja converter:
            
1 - Celsius
2 - Fahrenheit
3 - Kelvin"""
            opcao = lerOpcao(1, 3, menu)
            if opcao == 1:
                valorTemperatura = lerInt("Digite o valor da temperatura:")
                menu = """
Para qual temperatura deseja converter?
                
1 - Fahrenheit
2 - Kelvin"""
                opcao = lerOpcao(1, 2, menu)
                if opcao == 1:
                    resultadoConversao = int((valorTemperatura * 1.8) + 32)
                    print("")
                    print(f"\n{valorTemperatura}° Celsius é equivalente a {resultadoConversao}° Fahrenheit.\n")
                    print("")
                    time.sleep(2)
                elif opcao == 2:
                    resultadoConversao = valorTemperatura + 273.15
                    
                    print(f"\n{valorTemperatura}° Celsius é equivalente a {resultadoConversao}° Kelvin.\n")
                    time.sleep(2)

            elif opcao == 2:

                valorTemperatura = lerInt("Digite o valor da temperatura:")
                menu = """
print("Para qual temperatura deseja converter?")
                
1 - Celsius
2 - Kelvin"""
                opcao = lerOpcao(1, 2, menu)

                if opcao == 1:
                    resultadoConversao = int((valorTemperatura - 32) / 1.8)
                    print(f"\n{valorTemperatura}° Fahrenheit é equivalente a {resultadoConversao}° Celsius.\n")
                    time.sleep(2)

                elif opcao == 2:
                    resultadoConversao = int((valorTemperatura - 32) / 1.8) + 273.15
                    print(f"\n{valorTemperatura}° Fahrenheit é equivalente a {resultadoConversao}° Kelvin.\n")
                    time.sleep(2)

            elif opcao == 3:

                    valorTemperatura = lerInt("Digite o valor da temperatura:")
                    menu = """
print("Para qual temperatura deseja converter?")
                
1 - Celsius
2 - Fahrenheit"""
                    opcao = lerOpcao(1, 2, menu)

                    if opcao == 1:
                        resultadoConversao = valorTemperatura - 273.15
                        print(f"\n{valorTemperatura}° Kelvin é equivalente a {resultadoConversao}° Celsius.\n")
                        time.sleep(2)

                    elif opcao == 2:
                        resultadoConversao = int(((valorTemperatura - 273.15) * 1.8) + 32)
                        print(f"\n{valorTemperatura}° Kelvin é equivalente a {resultadoConversao}° Fahrenheit.\n")
                        time.sleep(2)

#----------------------------------CALCULADORA-DESCONTO----------------------------------------
def calculadoraDesconto():

    print("\nOlá! Seja bem-vindo(a) ao cálculo de desconto!\n")
    
    print("Insira o valor bruto:\n")
    valorBruto = int(input("R$"))


    print("\nInsira o desconto desejado:\n")
    desconto = int(input("%"))

    valorDesconto = valorBruto * (1 - (desconto/100))

    print(f"\nR${valorBruto:.2f} com {desconto}% de desconto fica R${valorDesconto:.2f}\n".replace('.', ','))
    voltar(2)
