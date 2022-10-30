t = "\n P = Paciente \n V = Visitante"
y = "\n L = Limpeza \n A = Administração"

resposta = input("Precisa de ajuda? ").upper()

if resposta == "NAO" or resposta == "NÃO":
    print("Otimo! Siga seu caminho.")
elif resposta != "NAO" and resposta != "NÃO" and resposta != "SIM":
    print("Invalido!")
else:
    while resposta == "SIM":       
        sexo = input("Você é homem ou mulher? ").upper()
        if sexo == "MULHER":
            print("Bem vinda")
            print(" F = Funcionária" + t)
        elif sexo == "HOMEM":
            print("Bem vindo")
            print(" F = Funcionário" + t)
        else:
            print("Invalido!")

        nivel = input("Digite o nivel de acesso: ").upper()

        if nivel == "F":
            if sexo == "MULHER":
                print(" M = Médica \n E = Enfermeira" + y)
            else:
                print(" M = Médico \n E = Enfermeiro" + y)
            categoria = input("Qual sua categoria? ").upper()

            ajudaLocal = input(
                "Precisa de ajuda para encontrar seu local de trabalho? ").upper()
            if ajudaLocal == "SIM":
                if categoria == "M" or categoria == "E":
                    print(" Dirija-se a aréa médica no 3º piso. \
                    \n Lá você encontrará informação específica sobre sua sala")
                    break
                elif categoria == "A":
                    print(" Dirija-se a aréa administrativa no 1º piso.")
                    break
                elif categoria == "L":
                    print(" Dirija-se a aréa de limpeza no 2º piso.")
                    break
                else:
                    print("Invalido!")            

        elif nivel == "P" or nivel == "V":
            if nivel == "V":
                print("Digite as informações da(o) paciente que deseja visitar.")           
            sexoV = input("O paciente é homem ou mulher? ").upper()
            idade = int(input("Digite a idade? "))            
            doença = input("Possui alguma doença?: ").upper()
            if idade < 65:
                if sexoV == "MULHER":
                    gestante = input("Está gravida? ").upper()

                    if gestante == "SIM" and doença == "SIM":
                        prioridade = "possui"
                        local = "área super especial"
                    elif gestante == "SIM" and doença == "NÃO":
                        prioridade = "possui"
                        local = "área de gestação"

                elif sexoV != "HOMEM" or sexoV != "MULHER":
                    print("Invalido!")

            elif idade >= 65 or doença == "SIM":
                prioridade = "possui"
                if doença == "SIM":
                    local = "área especial"
                else:
                    local = "área de idosos"
            else:
                prioridade = "não possui"
                local = "área normal"

        elif nivel != "P" or nivel != "V" or nivel != "F":
            print("Invalido!")

        if nivel == "P":
            print(" O paciente " + prioridade + " atendimento prioritário. \n" +
                  " Encaminhe-o para a " + local)
            break
        else:
            print(" O paciente " + prioridade + " atendimento prioritário. \n" +
                  " Ele está na " + local)
            break
