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
    print("5 - Sair")
    print("--------------------------------------------")
    operacao = int(input("| "))

    while operacao < 1 or operacao > 5:
        print("")
        print("Número inválido! Selecione uma opção existente")
        print("")
        print("1 - Sistema de Compra Lanchonete")
        print("2 - Calculadora Simples")
        print("3 - Cálculo Desconto")
        print("4 - Conversor de Temperatura")
        print("5 - Sair")
        print("")   
        operacao = int(input("| "))

    if operacao == 1:
        print("")
        print("Olá! Seja bem vindo(a) a nossa lanchonete! Qual será seu pedido?")
        print("")
        print("0 - Sair")
        print("1 - Hamburguer | R$20,00")
        print("2 - Refrigerante | R$7,00")
        print("3 - Batata Frita | R$12,00")
        print("4 - Finalizar")
        pedido = int(input("| "))

        valorPedido = int(0)
        while pedido > 0 and pedido < 4:
            if pedido == 1:
                valorPedido += 20
            if pedido == 2:
                valorPedido += 71
            if pedido == 3:
                valorPedido += 12
                print("")
            print("1 - Hamburguer | R$20,00")
            print("2 - Refrigerante | R$7,00")
            print("3 - Batata Frita | R$12,00")
            print("0 - Finalizar")
            pedido = int(input("| "))
        if pedido == 4:
            print("Pedido finalizado. Seu pedido ficou no valor de R$", valorPedido, ",00")
        if pedido == 0:
            operacao = 5




    if operacao == 2:
        print("Olá! Seja bem vindo a calculadora!")
        print("")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        calculoSelecionado = int(input("| "))

        if calculoSelecionado == 1:
            operacao = 5

        while calculoSelecionado < 1 or calculoSelecionado > 5:
            print("")
            print("Número inválido! Selecione uma opção existente")
            print("")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Sair")
            calculoSelecionado = int(input("| "))
        
        if calculoSelecionado == 1:
            nmr1 = int(input("Digite o primeiro número: "))
            nmr2 = int(input("Digite o segundo número: "))
            resultadoSoma = nmr1 + nmr2
            print(nmr1, " + ", nmr2, " = ", resultadoSoma)
        if calculoSelecionado == 2:
            nmr1 = int(input("Digite o primeiro número: "))
            nmr2 = int(input("Digite o segundo número: "))
            resultadoSubtracao = nmr1 - nmr2
            print(nmr1, " - ", nmr2, " = ", resultadoSubtracao)
        if calculoSelecionado == 3:
            nmr1 = int(input("Digite o primeiro número: "))
            nmr2 = int(input("Digite o segundo número: "))
            resultadoMultiplicacao = nmr1 * nmr2
            print(nmr1, " x ", nmr2, " = ", resultadoMultiplicacao)
        if calculoSelecionado == 4:
            nmr1 = int(input("Digite o primeiro número: "))
            nmr2 = int(input("Digite o segundo número: "))
            resultadoDivisao = nmr1 / nmr2
            print(nmr1, " / ", nmr2, " = ", resultadoDivisao)

    if operacao == 3:
        print("")
        print("Olá! Seja bem-vindo(a) ao cálculo de desconto.")

        print("Insira o valor bruto:")
        print("")
        valorBruto = int(input("R$"))

        print("")
        print("Insira o desconto desejado:")
        print("")
        desconto = int(input("%"))

        valorDesconto = valorBruto * (1 - (desconto/100))
        print("")

        print(f"R${valorBruto:.2f} com {desconto}% de desconto fica R${valorDesconto:.2f}".replace('.', ','))

        time.sleep(3)
        print("")


    if operacao == 4:
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

        while(temperaturaSelecionada < 0 and temperaturaSelecionada > 3):
            print("Valor inválido! Por favor, selecione uma opção correta:")
            print("")
            print("1 - Celsius")
            print("2 - Fahrenheit")
            print("3 - Kelvin")
            print("")
            print("0 - Sair")
            print("")
            temperaturaSelecionada = int(input("|"))

        
        if temperaturaSelecionada == 0:
            operacao = 5
        if temperaturaSelecionada == 1:

            print("")
            print("Digite a temperatura")
            print("")
            valorTemperatura = int(input("| "))

            print("")
            print("Para qual temperatura deseja converter?")
            print("")
            print("1 - Fahrenheit")
            print("2 - Kelvin")
            temperaturaConversao = int(input("| "))

            if temperaturaConversao == 1:
                resultadoConversao = int((valorTemperatura * 1.8) + 32)
                print("")
                print(f"{valorTemperatura}° Celsius é equivalente a {resultadoConversao}° Fahrenheit.")
                print("")
                time.sleep(2)

            if temperaturaConversao == 2:
                resultadoConversao = valorTemperatura + 273,15
                print("")
                print(f"{valorTemperatura}° Celsius é equivalente a {resultadoConversao}° Kelvin.")
                print("")
                time.sleep(2)
         

        if temperaturaSelecionada == 2:

            print("")
            print("Digite a temperatura")
            print("")
            valorTemperatura = int(input("| "))

            print("Para qual temperatura deseja converter?")
            print("")
            print("1 - Celsius")
            print("2 - Kelvin")
            temperaturaConversao = int(input("| "))

            if temperaturaConversao == 1:
                resultadoConversao = int((valorTemperatura - 32) / 1.8)
                print("")
                print(f"{valorTemperatura}° Fahrenheit é equivalente a {resultadoConversao}° Celsius.")
                print("")
                time.sleep(2)

            if temperaturaConversao == 2:
                resultadoConversao = int((valorTemperatura - 32) / 1.8) + 273.15
                print("")
                print(f"{valorTemperatura}° Fahrenheit é equivalente a {resultadoConversao}° Kelvin.")
                print("")
                time.sleep(2)

        if temperaturaSelecionada == 3:

            print("")
            print("Digite a temperatura")
            print("")
            valorTemperatura = int(input("| "))

            print("Para qual temperatura deseja converter?")
            print("")
            print("1 - Celsius")
            print("2 - Fahrenheit")
            print("")
            temperaturaConversao = int(input("| "))

            if temperaturaConversao == 1:
                resultadoConversao = valorTemperatura - 273.15
                print("")
                print(f"{valorTemperatura}° Kelvin é equivalente a {resultadoConversao}° Celsius.")
                print("")
                time.sleep(2)

            if temperaturaConversao == 2:
                resultadoConversao = int(((valorTemperatura - 273.15) * 1.8) + 32)
                print("")
                print(f"{valorTemperatura}° Kelvin é equivalente a {resultadoConversao}° Fahrenheit.")
                print("")
                time.sleep(2)




        

print("")
print("Você saiu.")

time.sleep(2)
print("")
