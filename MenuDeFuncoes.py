import time

operacao = int(1)

while operacao != 5:
    print("--------------------------------------------")
    print("MENU DE OPÇÕES - SELECIONE A OPÇÃO DESEJADA")
    print("")
    print("1 - Sistema de Compra Lanchonete")
    print("2 - Calculadora Simples")
    print("3 - Cálculo Desconto")
    print("4 - Conversor de Temperatura")
    print("5 - Calculo de Idade")
    print("0 - Sair")
    print("--------------------------------------------")
    operacao = int(input("| "))
    time.sleep(1)

    while operacao < 0 or operacao > 5:
        print("")
        print("Opção inválida! Selecione uma opção existente:")
        time.sleep(1)
        print("")
        print("1 - Sistema de Compra Lanchonete")
        print("2 - Calculadora Simples")
        print("3 - Cálculo Desconto")
        print("4 - Conversor de Temperatura")
        print("0 - Sair")
        print("")   
        operacao = int(input("| "))
        time.sleep(1)

    if operacao == 1:
        print("")
        print("Olá! Seja bem vindo(a) a nossa lanchonete! Qual será seu pedido?")
        print("")
        print("1 - Hamburguer | R$20,00")
        print("2 - Refrigerante | R$7,00")
        print("3 - Batata Frita | R$12,00")
        print("------------------------------")
        print("4 - Finalizar pedido")
        print("0 - Cancelar e sair")
        print("")
        pedido = int(input("| "))
        time.sleep(1)

        while pedido < 0 or pedido > 4:
            print("")
            print("Opção inválida! Selecione uma opção existente:")
            time.sleep(1)
            print("")
            print("1 - Hamburguer | R$20,00")
            print("2 - Refrigerante | R$7,00")
            print("3 - Batata Frita | R$12,00")
            print("------------------------------")
            print("4 - Finalizar pedido")
            print("0 - Cancelar e sair")
            print("")
            pedido = int(input("| "))


        valorPedido = int(0)
        while pedido > 0 and pedido < 4:
            if pedido == 1:
                print("")
                print("Hamburguer adicionado")
                print("")
                time.sleep(1)
                valorPedido += 20
            elif pedido == 2:
                valorPedido += 7
                print("")
                print("Refrigerante adicionado")
                print("")
                time.sleep(1)
            elif pedido == 3:
                print("")
                print("Batata Frita adicionada")
                print("")
                time.sleep(1)
                valorPedido += 12
            print("")
            print("0 - Cancelar e sair")
            print("")
            print("1 - Hamburguer | R$20,00")
            print("2 - Refrigerante | R$7,00")
            print("3 - Batata Frita | R$12,00")
            print("")
            print("4 - Finalizar e pagar")
            print("")
            pedido = int(input("| "))
            time.sleep(1)
        if pedido == 4:
            print("")
            print("Pedido finalizado. Seu pedido ficou no valor de R$", valorPedido, ",00")
            print("")
            time.sleep(2)
        elif pedido == 0:
            print("")
            print("Pedido cancelado. Voltando ao menu...")
            time.sleep(1)
            print("")
            operacao = 1




    elif operacao == 2:
        print("")
        print("Olá! Seja bem vindo a calculadora!")
        print("")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("------------------------------")
        print("0 - Sair")
        print("")
        calculoSelecionado = int(input("| "))
        time.sleep(1)

        if calculoSelecionado == 0:
            
            print("")
            print("Voltando ao menu...")
            print("")
            time.sleep(2)
            
            operacao = 1

        while calculoSelecionado < 1 or calculoSelecionado > 5:
            print("")
            print("Opção inválida! Selecione uma opção existente:")
            time.sleep(1)
            print("")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("------------------------------")
            print("0 - Sair")
            calculoSelecionado = int(input("| "))
            time.sleep(1)
        
        if calculoSelecionado == 1:
            print("")
            nmr1 = int(input("Digite o primeiro número: "))
            print("")
            nmr2 = int(input("Digite o segundo número: "))
            print("")
            resultadoSoma = nmr1 + nmr2
            print(nmr1, " + ", nmr2, " = ", resultadoSoma)
            time.sleep(2)
        elif calculoSelecionado == 2:
            print("")
            nmr1 = int(input("Digite o primeiro número: "))
            print("")
            nmr2 = int(input("Digite o segundo número: "))
            print("")
            resultadoSubtracao = nmr1 - nmr2
            print(nmr1, " - ", nmr2, " = ", resultadoSubtracao)
            time.sleep(2)
        elif calculoSelecionado == 3:
            print("")
            nmr1 = int(input("Digite o primeiro número: "))
            print("")
            nmr2 = int(input("Digite o segundo número: "))
            print("")
            resultadoMultiplicacao = nmr1 * nmr2
            print(nmr1, " x ", nmr2, " = ", resultadoMultiplicacao)
            time.sleep(2)
        elif calculoSelecionado == 4:
            print("")
            nmr1 = int(input("Digite o primeiro número: "))
            print("")
            nmr2 = int(input("Digite o segundo número: "))
            print("")
            resultadoDivisao = int(nmr1 / nmr2)
            print(nmr1, " / ", nmr2, " = ", resultadoDivisao)
            time.sleep(2)

    elif operacao == 3:
        print("")
        print("Olá! Seja bem-vindo(a) ao cálculo de desconto!")
        time.sleep(2)
        print("Insira o valor bruto:")
        print("")
        valorBruto = int(input("R$"))
        time.sleep(1)

        print("")
        print("Insira o desconto desejado:")
        print("")
        desconto = int(input("%"))
        time.sleep(1)

        valorDesconto = valorBruto * (1 - (desconto/100))
        print("")
        print(f"R${valorBruto:.2f} com {desconto}% de desconto fica R${valorDesconto:.2f}".replace('.', ','))
        time.sleep(3)
        print("")


    elif operacao == 4:
        print("")
        print("Seja bem-vindo(a) ao conversor de temperatura! Selecione a unidade que deseja converter:")
        print("")
        print("1 - Celsius")
        print("2 - Fahrenheit")
        print("3 - Kelvin")
        print("")
        print("0 - Sair")
        print("")
        temperaturaSelecionada = int(input("|"))

        while(temperaturaSelecionada < 0 or temperaturaSelecionada > 3):
            print("")
            print("Opção inválida! Selecione uma opção existente:")
            time.sleep(1)
            print("")
            print("1 - Celsius")
            print("2 - Fahrenheit")
            print("3 - Kelvin")
            print("")
            print("0 - Sair")
            print("")
            temperaturaSelecionada = int(input("|"))
            time.sleep(1)


        
        if temperaturaSelecionada == 0:
            print("")
            print("Voltando ao menu...")
            print("")
            time.sleep(2)
            
            operacao = 1
        elif temperaturaSelecionada == 1:

            print("")
            print("Digite a temperatura")
            print("")
            valorTemperatura = int(input("| "))
            time.sleep(1)

            print("")
            print("Para qual temperatura deseja converter?")
            print("")
            print("1 - Fahrenheit")
            print("2 - Kelvin")
            print("")
            temperaturaConversao = int(input("| "))
            time.sleep(1)

            while temperaturaConversao < 1 or temperaturaConversao > 2:
                print("")
                print("Opção inválida! Selecione uma opção existente:")
                time.sleep(1)
                print("")
                print("1 - Fahrenheit")
                print("2 - Kelvin")
                print("")
                temperaturaConversao = int(input("| "))
                time.sleep(1)

            if temperaturaConversao == 1:
                resultadoConversao = int((valorTemperatura * 1.8) + 32)
                print("")
                print(f"{valorTemperatura}° Celsius é equivalente a {resultadoConversao}° Fahrenheit.")
                print("")
                time.sleep(2)

            elif temperaturaConversao == 2:
                resultadoConversao = valorTemperatura + 273.15
                print("")
                print(f"{valorTemperatura}° Celsius é equivalente a {resultadoConversao}° Kelvin.")
                print("")
                time.sleep(2)
         

        elif temperaturaSelecionada == 2:

            print("")
            print("Digite a temperatura")
            print("")
            valorTemperatura = int(input("| "))
            time.sleep(1)

            print("Para qual temperatura deseja converter?")
            print("")
            print("1 - Celsius")
            print("2 - Kelvin")
            print("")
            temperaturaConversao = int(input("| "))
            time.sleep(1)

            while temperaturaConversao < 1 or temperaturaConversao > 2:
                print("")
                print("Opção inválida! Selecione uma opção existente:")
                time.sleep(1)
                print("")
                print("1 - Fahrenheit")
                print("2 - Kelvin")
                print("")
                temperaturaConversao = int(input("| "))

            if temperaturaConversao == 1:
                resultadoConversao = int((valorTemperatura - 32) / 1.8)
                print("")
                print(f"{valorTemperatura}° Fahrenheit é equivalente a {resultadoConversao}° Celsius.")
                print("")
                time.sleep(2)

            elif temperaturaConversao == 2:
                resultadoConversao = int((valorTemperatura - 32) / 1.8) + 273.15
                print("")
                print(f"{valorTemperatura}° Fahrenheit é equivalente a {resultadoConversao}° Kelvin.")
                print("")
                time.sleep(2)

        elif temperaturaSelecionada == 3:

            print("")
            print("Digite a temperatura")
            print("")
            valorTemperatura = int(input("| "))
            time.sleep(1)

            print("Para qual temperatura deseja converter?")
            print("")
            print("1 - Celsius")
            print("2 - Fahrenheit")
            print("")
            temperaturaConversao = int(input("| "))
            time.sleep(1)

            while temperaturaConversao < 1 or temperaturaConversao > 2:
                print("")
                print("Opção inválida! Selecione uma opção existente:")
                time.sleep(1)
                print("")
                print("1 - Fahrenheit")
                print("2 - Kelvin")
                print("")
                temperaturaConversao = int(input("| "))
                time.sleep(1)

            if temperaturaConversao == 1:
                resultadoConversao = valorTemperatura - 273.15
                print("")
                print(f"{valorTemperatura}° Kelvin é equivalente a {resultadoConversao}° Celsius.")
                print("")
                time.sleep(2)

            elif temperaturaConversao == 2:
                resultadoConversao = int(((valorTemperatura - 273.15) * 1.8) + 32)
                print("")
                print(f"{valorTemperatura}° Kelvin é equivalente a {resultadoConversao}° Fahrenheit.")
                print("")
                time.sleep(2)
    

    elif operacao == 5:
        print("")
        print("Seja bem-vindo(a) a calculadora de idade")
        print("Escreva seu ano de nascimento")
        print("")
        anoNascimento = int(input("| "))
        time.sleep(1)

        print("")
        print("Escreva o ano atual")
        print("")
        anoAtual = int(input("| "))
        time.sleep(1)

        print("")
        print("Fez aniversário esse ano?")
        print("1 - Sim")
        print("2 - Não")
        print("")
        fezAniversario = int(input("| "))
        time.sleep(1)

        while fezAniversario < 1 or fezAniversario > 2:
            print("")
            print("Opção inválida! Selecione uma opção existente:")
            time.sleep(1)
            print("")
            print("Fez aniversário esse ano?")
            print("1 - Sim")
            print("2 - Não")
            print("")
            fezAniversario = int(input("| "))


        if fezAniversario == 1:
            idade = anoAtual-anoNascimento
            print(f"Sua idade é {idade}.")
            print("")
            time.sleep(2)
            
        elif fezAniversario == 2:
            time.sleep(2)
            idade = (anoAtual - anoNascimento) - 1
            print(f"Sua idade é {idade}.")
            print("")
            time.sleep(2)

    elif operacao == 0:
        break



        

print("")
print("Você saiu.")

time.sleep(2)
print("")
